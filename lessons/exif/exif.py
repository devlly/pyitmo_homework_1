from PIL import Image
from PIL.ExifTags import TAGS
import os.path
import re
import webbrowser


class CustomException(Exception):
    pass

class Img():
    """
    Class Image
    path - way to the image in jpg format
    """

    def __init__(self, path, info=None, meta=None, name = None):
        self.path = path
        self.info = {}
        self.meta = {}
        self.name = self.path.rstrip('.jpg') + '.txt'


    def get_metadata(self):
        """Extract metadata to the dictionary and write data to the file """
        try:
            f = Image.open(self.path)
            print('Checking for metadata...')
            self.meta = f._getexif()
            if self.meta:
                print('MetaData were found!')
                for tag, value in self.meta.items():
                    tagname = TAGS.get(tag, tag)
                    self.info[tagname] = value
                print('Metadata were written to {} file'.format(self.name))
                with open(self.name, 'w') as f:
                    for tagname, value in self.info.items():
                        f.write(str(tagname)+'\t'+\
                                str(value)+'\n')
        except:
            raise CustomException('Impossible to excract metadata: no data!')



    def check_geo(self):
        """Try to extract GPS data and make the point in openstreetmap"""
        try:
            with open(self.name) as f:
                for line in f:
                    if 'GPS' in line:
                        line = re.sub('[(())]', '', line)
                        line = re.split(r', \d+:', line)
                        lon = line[2]
                        lat = line[4]
                        coord = []
                        for i in lon, lat:
                            i = i.split(',')[::2]
                            i = int(i[0])+(int(i[1])/60.0)+(int(i[2])/3600.0)
                            coord.append(i)

                        a, b = coord
                        st = 'http://openstreetmap.org/search?query={}%2C{}'.format(a, b)
                        webbrowser.open(st)
        except:
            raise CustomException('Impossible to show geolocation: no GPS data!')

    def check_model(self):
        """Try to extract info about model of the photocamera and search in duckduckgo"""
        try:
            with open(self.name) as f:
                for line in f:
                    if 'Model' in line:
                        line = line.lstrip('Model')
                        line = line.lstrip(' ')
                        line = re.sub(' ', '+', line)
                        st = 'https://duckduckgo.com/?q='+line
                        webbrowser.open(st)
        except:
            raise CustomException('Impossible to show camera model: no data!')



class Main():
    """Show menu"""

    def show_menu():
        print('''
        1. Write 1 to get MetaData
        2. Write 2 to get GeoData
        3. Write 3 to check Camera's model
        4. Write 3 to exit''')

    def execute():
        cmd = int(input('write command\n'))
        if cmd == 1:
            path = input('Write file name\n')
            img1 = Img(path)
            img1.get_metadata()

        if cmd == 2:
            path = input('Write file name\n')
            img1 = Img(path)
            img1.get_metadata()
            img1.check_geo()

        if cmd == 3:
            path = input('Write file name\n')
            img1 = Img(path)
            img1.get_metadata()
            img1.check_model()

        if cmd == 4:
            pass
