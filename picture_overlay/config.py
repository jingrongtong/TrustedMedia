# Get environment variables
import os

HOME = os.getenv('HOME')
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(FILE_DIR, "../data/")
RAW_PICTURES_DIR = os.path.abspath(os.path.join(DATA_DIR, "raw_pictures"))
