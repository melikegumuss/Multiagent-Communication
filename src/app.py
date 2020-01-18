from flask import Flask, jsonify, request, json
from publisher_manager import PublisherManager
from subscriber_manager import SubscriberManager

app = Flask(__name__)
publisher_manager = PublisherManager.get_instance()
subscriber_manager = SubscriberManager.get_instance()

# TEST PARAMETERS:
# {   "name": "task_manager", "topics": ["visiting", "excavation"]}
# {   "name": "drone", "topics": ["visiting"]}
# {   "name": "mas", "topics": ["visiting", "excavation"]}
# {   "topic_name": "visiting", "data": {"control_point_x": 4, "control_point_y": 5}}
# {"id": 0}

#   task_manager
#   ['visiting', 'excavation']
#

# TODO: - remove ve delete metodlarını da implementle topic için gerekli mi?
# TODO: MOST IMPORTANT, RETURN EDİLEN JSON GÖRÜNÜMLERİNİ DÜZENLE!!!!!!!!!!
# TODO: COMMENTS!!!!
# TODO: minik buglar
# TODO: log ile alakalı manager yap
# TODO: UNIT TEST


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"greeting": "hello!"})


@app.route('/publisher', methods=['POST'])
def register_publisher():
    if request.method == "POST":
        name = request.json['name']
        topics = request.json['topics']
        p = publisher_manager.add_publisher(name, topics)
        return jsonify({'id': p.get_id()})


@app.route('/subscriber', methods=['POST'])
def register_subscriber():
    if request.method == 'POST':
        name = request.json['name']
        topics = request.json['topics']
        s = subscriber_manager.add_subscriber(name, topics)
        return jsonify({'id': s.get_id()})


@app.route('/publisher', methods=['DELETE'])
def unregister_publisher():
    if request.method == 'DELETE':
        id_ = request.json['id']
        p = publisher_manager.remove_publisher(id_)
        return "Publisher removal successful!" + str(p)


@app.route('/subscriber', methods=['DELETE'])
def unregister_subscriber():
    if request.method == 'DELETE':
        id_ = request.json['id']
        s = subscriber_manager.remove_subscriber(id_)
        return "Subscriber removal successful!" + str(s)


@app.route('/publish', methods=['POST'])
def publish():
    print("if üstü")
    if request.method == 'POST':
        print("if içi")
        topic_name = request.json['topic_name']
        print(topic_name)
        print("topic name altı")
        data = request.json['data']
        print(data)
        print("data altı")
        publisher_manager.publish(topic_name, data)
        return 'Publishing on topic \'{0}\' successful!'.format(topic_name)
    return "Başarısız".format("UI2Task")

# @app.route('/publishing/<string:topic_name>/<int:sub_id>', methods=['GET'])
# def receive_topic_data(topic_name, sub_id):
#     if request.method == 'GET':
#         return jsonify(sm.receive_topic_message(topic_name, sub_id))


@app.route('/publish/<int:sub_id>', methods=['GET'])
def receive_all_data(sub_id):
    if request.method == 'GET':
        data = subscriber_manager.receive_messages(sub_id).copy()
        # CLEAR MESSAGE LIST OF SUBSCRIBER
        subscriber_manager.clear_messages(sub_id)
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# tbtk ip: '10.40.4.56'
# openVPN ip: '10.1.43.5'
