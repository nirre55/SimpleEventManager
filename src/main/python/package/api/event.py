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
        with open(self.path(), "r") as f:
            json_load = json.load(f)
        data = json_load["events"]

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
        if not os.path.isfile(self.path()):
            data = {"events": []}
            with open(self.path(), "w") as f:
                json.dump(data, f, indent=4)
        else:
            print("os.path.isfile(self.path)")






    #add new data on the JSON file
    def addData(self, data):
        self.save()

        with open(self.path(), "r+") as f:
            file_data = json.load(f)
            file_data["events"].append(data)
            f.seek(0)
            json.dump(file_data, f, indent=4, default=self.myconverter)



if __name__ == '__main__':
    event = Event()
    data_id = {"id": event.get_id_event}
    data = {"title": "rakan", "content": "soug", "start_date": "1998/05/05 01:00:00", "end_date": "2000/05/05 01:00:00", "timezone": event.time_zone}
    data_id.update(data)
    print(data_id)
    event.addData(data_id)






