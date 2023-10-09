class Album:
    def __init__(self):
        self.name = ""
        self.id_album = 0

    def __init__(self, name, id_album):
        self.name = name
        self.id_album = id_album

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id_album(self):
        return self.id_album

    def set_id_album(self, id_album):
        self.id_album = id_album