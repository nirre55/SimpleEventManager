import os
import json

from datetime import datetime
import tzlocal as tzlocal

from package.api.constants import EVENTS_DIR, EVENTS_DIR_ID

class Event:
    def __init__(self, id_event=0, title="", content="", start_date="", end_date=""):
        self.id_event = id_event
        self.title = title
        self.content = content
        self.start_date = start_date
        self.end_date = end_date
        self.time_zone = datetime.now(tzlocal.get_localzone()).strftime('%Z')


    def __str__(self):
        return f"\"id\": {self.id_event}, \"title\": \"{self.title}\", \"content\": \"{self.content}\", \"start_date\": \"{self.start_date}\", \"end_date\": \"{self.end_date}\", \"timezone\": \"{self.time_zone}\""

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value


    #get the path of the JSON file
    def path(self):
        return os.path.join(EVENTS_DIR, EVENTS_DIR_ID + ".json")


    #get the last id_event on the file and add 1 to id
    @property
    def get_id_event(self):
        if os.stat(self.path()).st_size == 0:
            return 0
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]
        if (len(data) == 0):
            return 0
        return data[-1]["id"] + 1


    def get_info_id(self, id_value):
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]
        if (id_value >= len(data)):
            return "Error: id doesn't exist"
        else:
            return data[id_value]

    #to serialize a datetime object as JSON
    def myconverter(self, o):
        if isinstance(o, datetime):
            return o.__str__()


    #create a file/directory(if not exist) and add events array on the JSON file
    def save(self):
        if not os.path.exists(EVENTS_DIR):
            os.makedirs(EVENTS_DIR, exist_ok=True)
            data = {"events": []}
            with open(self.path(), "w+") as f:
                json.dump(data, f, indent=4)
        else:
            print("os.path.isfile(self.path)")



    #add new data on the JSON file
    def addData(self, data):
        with open(self.path(), "r+") as f:
            file_data = json.load(f)
            file_data["events"].append(data)
            f.seek(0)
            json.dump(file_data, f, indent=4, default=self.myconverter)


    #update data on the JSON file with new informations
    def updateData(self, id_value, data_to_update=None):
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]
        if (id_value >= len(data)):
            return {"Error": "id doesn't exist"}
        else:
            key_list = list(data_to_update.keys())
            val_list = list(data_to_update.values())
            for i in range(len(key_list)):
                json_load["events"][id_value][key_list[i]] = val_list[i]

            with open(self.path(), "w") as f:
                json.dump(json_load, f, indent=4)
            return {"Response": "done!"}


    def deleteData(self, id_value):
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]
        if (id_value >= len(data)):
            return {"Error": "id doesn't exist"}
        else:
            del json_load["events"][id_value]
            with open(self.path(), "w") as f:
                json.dump(json_load, f, indent=4)
            self.update_id()
            return {"Response": "done!"}

    def update_id(self):
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]
        for i in range(len(data)):
            json_load["events"][i]["id"] = i
        with open(self.path(), "w") as f:
            json.dump(json_load, f, indent=4)










if __name__ == '__main__':
    event = Event()
"""
    # create folder and json file
    event.save()
    # create dictionnary of data
    data = {"id": event.get_id_event, "title": "Festival de music 3", "content": "Lancement du plus grand festivale de music 3", "start_date": "2023/01/01 15:00:00", "end_date": "2023/01/30 15:00:00", "timezone": event.time_zone}
    # add data to the json file
    event.addData(data)

"""





