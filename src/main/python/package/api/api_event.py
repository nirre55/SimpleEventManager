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
    try:
        return jsonify(ev.get_info_id(int(id_event)))
    except Exception as e:
        return jsonify({"Error": str(e)})


@app.route('/api/v1/resources/events', methods=['POST'])
def add_event():
    try:
        title = {"title": request.json["title"]}
        content = {"content": request.json["content"]}
        start_date = {"start_date": request.json["start_date"]}
        end_date = {"end_date": request.json["end_date"]}

        data = {"id": ev.get_id_event}
        data.update(title)
        data.update(content)
        data.update(start_date)
        data.update(end_date)
        data.update({"timezone": ev.time_zone})

        ev.addData(data)
        # app.logger.info(ev)
        return jsonify({"Response": "DONE!"})
    except Exception as e:
        return jsonify({"Error": str(e)})



@app.route('/api/v1/resources/events', methods=['PUT'])
def update_event():
    try:
        query_parameters = request.args
        id_event = query_parameters.get('id')

        data = request.get_json(force=True)
        response = ev.updateData(int(id_event), data)

        return jsonify(response)
    except Exception as e:
        return jsonify({"Error": str(e)})


@app.route('/api/v1/resources/events', methods=['DELETE'])
def delete_event():
    try:
        query_parameters = request.args
        id_event = query_parameters.get('id')

        response = ev.deleteData(int(id_event))
        return jsonify(response)
    except Exception as e:
        return jsonify({"Error": str(e)})



if __name__ == '__main__':
    app.run(debug=True)

