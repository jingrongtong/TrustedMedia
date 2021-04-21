# This is a sample Python script.
import config
from CameraStub import CameraStub
from datetime import datetime
from yaml import load, dump

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_path(name, path):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name} : {path}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_timestamp():
    date_time = datetime.now()
    return date_time.strftime("%d_%m_%y_%H_%M_%S")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_path("Raw pictures directory", config.RAW_PICTURES_DIR)
    filename = config.RAW_PICTURES_DIR + "/" + "picture_" + get_timestamp() + ".jpg"
    stream = open('document.yaml', 'w')
    Camera = CameraStub()
    picture_metadata, picture = Camera.take_picture()
    picture.save(filename)
    dump(picture_metadata, stream)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
