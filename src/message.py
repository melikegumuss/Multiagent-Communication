class Message:
    def __init__(self, data):
        self.data = data

    def return_as_dict(self):
        return {"data": self.data}
