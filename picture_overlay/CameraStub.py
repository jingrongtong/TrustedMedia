import Metadata
from PIL import Image
import imagehash
import config


class CameraStub:
    def __init__(self):
        self.MetaCamera = MetaCameraStub()
        self.CMOSCamera = CMOSCameraStub()

    def take_picture(self):
        picture = self.CMOSCamera.take_picture()
        metadata = self.MetaCamera.take_picture(picture)
        return metadata, picture


class CMOSCameraStub:

    def __init__(self):
        self.mode = 'RGB'
        self.size = (720, 720)
        self.color = 'red'

    def take_picture(self):
        img = Image.new(self.mode, self.size, self.color)
        return img


class MetaCameraStub:

    def __init__(self):
        self.camera_name = "camera_stub"
        self.focal_distance = 1.0
        self.zoom_in = 1.0
        self.resolution = 3145728
        self.sensor_type = "CMOS"

    def take_picture(self, picture):
        picture_hash = imagehash.phash(Image.open(config.RAW_PICTURES_DIR + "/test_car_fire.jpg"), hash_size=64)
        print(picture_hash)
        metadata = Metadata.Metadata(picture_hash=picture_hash.__str__())
        return metadata
