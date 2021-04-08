import time
import Metadata


class CameraStub():

    def __init__(self):
        self.camera_name = "camera_stub"
        self.focal_distance = 1.0
        self.zoom_in = 1.0
        self.resolution = 3145728
        self.sensor_type = "CMOS"

    def take_picture(self):
        metadata = Metadata.Metadata()
        return metadata

