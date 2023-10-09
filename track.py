class Track:
    def __init__(self):
        self.name = ""
        self.id_album = 0
        self.id_genre = 0
        self.duration = 0
        self.size = 0
        self.price = 0

    def __init__(self, name, id_album, id_genre, duration, size, price):
        self.name = name
        self.id_album = id_album
        self.id_genre = id_genre
        self.duration = duration
        self.size = size
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id_album(self):
        return self.id_album

    def set_id_album(self, id_album):
        self.id_album = id_album

    def get_id_genre(self):
        return self.id_genre

    def set_id_genre(self, id_genre):
        self.id_genre = id_genre

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price