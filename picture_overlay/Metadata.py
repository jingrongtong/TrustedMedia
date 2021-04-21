import time


class Author:
    def __init__(self):
        self.first_name = "Hadrien"
        self.last_name = "Marcellin"


class GPS:
    def __init__(self):
        self.longitude = 92
        self.latitude = 5
        self.altitude = 600


class Location:
    def __init__(self):
        self.gps = GPS()
        self.hemisphere = "NORTH"
        self.post_code = 1005
        self.city = "Lausanne"
        self.street = "Avenue Charles Secrétan"
        self.number = 1


class Time:
    def __init__(self):
        self.time = time.localtime()


class Device:
    def __init__(self):
        self.brand = "APPLE"
        self.model = "Iphone 11 pro"
        self.operating_system = "OS 11"


class Image:
    def __init__(self, picture_hash):
        self.height = 1024
        self.width = 720
        self.encoding = "utf-8"
        self.color_palette = None
        self.format = None
        self.size = None
        self.key_words = None
        self.picture_hash = picture_hash


class Metadata:
    def __init__(self, picture_hash):
        self.author = Author()
        self.location = Location()
        self.device = Device()
        self.image = Image(picture_hash=picture_hash)
        self.time = Time()
        self.meta_hash = self.__hash__()

