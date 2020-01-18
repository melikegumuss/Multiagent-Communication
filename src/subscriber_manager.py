from subscriber import Subscriber
from topic_manager import TopicManager


class SubscriberManager:
    __instance = None
    sub_id = 0
    topic_manager = TopicManager.get_instance()

    def __init__(self):
        self.subscribers = {}
        if SubscriberManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SubscriberManager.__instance = self

    @staticmethod
    def get_instance():
        if SubscriberManager.__instance is None:
            SubscriberManager()
        return SubscriberManager.__instance

    def add_subscriber(self, name_, topics):
        j = 0
        name_found = False
        while j < len(self.subscribers):
            if name_ == self.subscribers.get(j).get_name():
                name_found = True
                break
            else:
                j += 1

        if not name_found:
            s = Subscriber(self.sub_id, name_)
            self.subscribers[s.get_id()] = s
            self.sub_id += 1

            i = 0
            while i < len(topics):
                if topics[i] not in self.topic_manager.topics:
                    self.topic_manager.add_sub(s, self.topic_manager.create_topic(topics[i]))
                else:
                    self.topic_manager.add_sub(s, self.topic_manager.find_topic(topics[i]))
                i += 1
            return s
        else:
            raise Exception("There is already a subscriber named \'{0}\' registered to topics \'{1}\'!".format(name_, topics))

    def remove_subscriber(self, input_id):
        if input_id in self.subscribers:
            self.subscribers.pop(input_id)
            s = self.topic_manager.remove_sub(input_id)
            # self.sub_id = 0
            return s
        else:
            raise Exception("There is no subscriber with the given ID!")

    # def receive_topic_message(self, topic_name, sub_id):
    #     if (topic_name in self.tm.topics) & (sub_id in self.tm.topics[topic_name].subscribers):
    #         print(self.tm.topics[topic_name].subscribers[sub_id].message_data[topic_name].get_datalist())
    #         return self.tm.topics[topic_name].subscribers[sub_id].message_data[topic_name].get_datalist()
    #     else:
    #         return 0

    def receive_messages(self, sub_id):
        if sub_id in self.subscribers:
            # print(self.subscribers[sub_id].get_message_data().values())
            return self.subscribers[sub_id].get_message_data()
        else:
            # print("else")
            return None

    def clear_messages(self, sub_id):
        if sub_id in self.subscribers:
            self.subscribers[sub_id].clear_message_data()
