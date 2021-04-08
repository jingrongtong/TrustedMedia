# This is a sample Python script.
import config
import CameraStub
import sys
from yaml import load, dump

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_path(name, path):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name} : {path}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_path("Raw pictures directory", config.RAW_PICTURES_DIR)

    stream = open('document.yaml', 'w')
    Camera = CameraStub.CameraStub()
    PictureMetadata = Camera.take_picture()
    dump(PictureMetadata, stream)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
