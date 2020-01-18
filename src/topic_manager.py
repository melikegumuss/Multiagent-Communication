from topic import Topic


class TopicManager:

    __instance = None

    def __init__(self):
        self.topics = {}
        if TopicManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TopicManager.__instance = self

    @staticmethod
    def get_instance():
        if TopicManager.__instance is None:
            TopicManager()
        return TopicManager.__instance

    def create_topic(self, name):
        t = Topic(name)
        self.topics[t.get_name()] = t
        return t

    def find_topic(self, topic):
        if topic in self.topics:
            return self.topics[topic]
        else:
            return None

    def add_pub(self, publisher, topic):
        self.topics.get(topic.get_name()).publishers.append(publisher)

    def add_sub(self, subscriber, topic):
        self.topics.get(topic.get_name()).subscribers.append(subscriber)

    def remove_pub(self, pub_id):
        for topic in self.topics:
            j = 0
            while pub_id != self.topics[topic].publishers[j].get_id():
                j += 1
            p = self.topics[topic].publishers.pop(j)
        return p

    def remove_sub(self, sub_id):
        for topic in self.topics:
            j = 0
            while sub_id != self.topics[topic].subscribers[j].get_id():
                j += 1
            s = self.topics[topic].subscribers.pop(j)
        return s
