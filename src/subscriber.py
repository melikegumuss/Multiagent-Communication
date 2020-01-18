class Subscriber:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
        self.message_data = {}

    def get_id(self):
        return self.id_

    def get_name(self):
        return self.name

    def get_message_data(self):
        data = {}
        for key in self.message_data:
            data[key] = self.message_data[key].return_as_dict()
        return data

    def clear_message_data(self):
        self.message_data.clear()
