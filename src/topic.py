class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.publishers = []

    def get_name(self):
        return self.name

    def get_publishers_list(self):
        return self.publishers

    def get_subscribers_list(self):
        return self.subscribers
