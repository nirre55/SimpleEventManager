import json
from flask import Flask, request, jsonify
from package.api.event import Event

ev = Event()
test = []

app = Flask(__name__)

@app.route('/')
def index():
    with open(ev.path(), "r+") as f:
        json_load = json.load(f)
    data = json_load["events"]
    return jsonify(data)


@app.route('/api/v1/resources/events', methods=['GET'])
def get_event_id():
    query_parameters = request.args
    id_event = query_parameters.get('id')
    return jsonify(ev.get_info_id(int(id_event)))

@app.route('/api/v1/resources/events/add', methods=['POST'])
def add_event():
    title = {"title":  request.json["title"]}
    content = {"content":  request.json["content"]}
    start_date = {"start_date":  request.json["start_date"]}
    end_date = {"end_date":  request.json["end_date"]}

    event = Event()

    data = {"id": event.get_id_event}
    data.update(title)
    data.update(content)
    data.update(start_date)
    data.update(end_date)
    data.update({"timezone": event.time_zone})

    event.addData(data)
    app.logger.info(event)
    return jsonify({"Response": "DONE!"})




if __name__ == '__main__':
    app.run(debug=True)

