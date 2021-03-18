from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import piexif
import numpy as np


class ImageGenerator:
    
    root = "/home/hadrien/AnacondaProjects/TrustedMedia/data/"
    
    def __init__(self, filename):
        self.filename = self.root + filename
        self.image = None
        self.exif_dict = None
       
    
    def load_image(self):
        self.image = Image.open(self.filename)
    
    
    def load_exif(self):
        try:
            self.exif_dict = piexif.load(self.image.info["exif"])
        except:
            self.exif_dict = dict({'0th': {}, 'Exif': {}, 'GPS': {}, 'Interop': {}, '1st': {}, 'thumbnail': {}})
    
    
    def load_image_file(self):
        self.load_image()
        self.load_exif()
        return self.image, self.exif_dict
    
    
    def add_exif(self, exif_data):
        for exif_main_key, data in exif_data.items() : 
            for key, value in data.items():
                self.exif_dict[exif_main_key][key] = value
                
    def save_to_file(self, filename):
        if self.exif_dict["thumbnail"] in [dict(), {}, None]:
            del self.exif_dict["thumbnail"]
            del self.exif_dict["1st"]
          
        exif_bytes = piexif.dump(self.exif_dict)
        self.image.save(self.root + filename, "jpeg", exif=exif_bytes)
        
        
    def display(self):
        print("7B Blvd de Rochechouart, 75009 Paris")
        print("{0} {1}.\n{2} {3}, {4} {5}, {6} {7}".format(piexif.TAGS['Image'][piexif.ImageIFD.DateTime]['name'],
                                                 self.exif_dict['0th'][piexif.ImageIFD.DateTime],
                                                 piexif.TAGS['GPS'][piexif.GPSIFD.GPSAltitude]['name'],
                                                 self.exif_dict['GPS'][piexif.GPSIFD.GPSAltitude],
                                                 piexif.TAGS['GPS'][piexif.GPSIFD.GPSLatitude]['name'],
                                                 self.exif_dict['GPS'][piexif.GPSIFD.GPSLatitude],
                                                 piexif.TAGS['GPS'][piexif.GPSIFD.GPSLongitude]['name'],
                                                 self.exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]))
        plt.figure(figsize=(20,10))
        plt.axis('off')
        plt.imshow(np.asarray(self.image))

        
        
                
                
class ExifGenerator:
    
    def __init__(self, exif_data=None):
        if exif_data:
            self.exif_dict = exif_data
        else:
            self.exif_dict = dict({'0th': {}, 'Exif': {}, 'GPS': {}, 'Interop': {}, '1st': {}, 'thumbnail': {}})
        
        
    def add_exif(self, exif_key, exif_code, value):
        self.exif_dict[exif_key][exif_code] = value
        
    
    
    
    
    
    
    
    
        