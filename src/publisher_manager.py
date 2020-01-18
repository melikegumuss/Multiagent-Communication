from publisher import Publisher
from topic_manager import TopicManager
from message import Message


class PublisherManager:

    __instance = None
    pub_id = 0
    topic_manager = TopicManager.get_instance()

    def __init__(self):
        self.publishers = {}
        if PublisherManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PublisherManager.__instance = self

    @staticmethod
    def get_instance():
        if PublisherManager.__instance is None:
            PublisherManager()
        return PublisherManager.__instance

    def add_publisher(self, name_, topics):
        j = 0
        name_found = False
        while j < len(self.publishers):
            if name_ == self.publishers.get(j).get_name():
                name_found = True
                break
            else:
                j += 1

        if not name_found:
            p = Publisher(self.pub_id, name_)
            self.publishers[p.get_id()] = p
            self.pub_id += 1

            i = 0
            while i < len(topics):
                if topics[i] not in self.topic_manager.topics:
                    self.topic_manager.add_pub(p, self.topic_manager.create_topic(topics[i]))
                else:
                    self.topic_manager.add_pub(p, self.topic_manager.find_topic(topics[i]))
                i += 1
            return p
        else:
            raise Exception("There is already a publisher named \'{0}\' registered to topics \'{1}\'!".format(name_, topics))

    def remove_publisher(self, input_id):
        if input_id in self.publishers:
            self.publishers.pop(input_id)
            p = self.topic_manager.remove_pub(input_id)
            # self.pub_id = 0
            return p
        else:
            raise Exception("There is no publisher with the given ID!")

    def publish(self, topic_name, data):
        if topic_name in self.topic_manager.topics:
            print(len(self.topic_manager.topics[topic_name].subscribers))
            if len(self.topic_manager.topics[topic_name].subscribers) > 0:
                i = 0
                message = Message(data)
                while i < len(self.topic_manager.topics[topic_name].subscribers):
                    self.topic_manager.topics[topic_name].subscribers[i].message_data[topic_name] = message
                    i += 1
            else:
                raise Exception("There is no subscriber assigned to the topic \'{0}\'!".format(topic_name))
        else:
            raise Exception("There is no topic \'{0}\'!".format(topic_name))
