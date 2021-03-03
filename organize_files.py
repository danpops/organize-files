import os
import glob
import shutil

path_to_source = '/path/to/Downloads/'

my_dict = {
    '/path/to/Documents': ['docx', 'doc', 'pdf', 'xls', 'txt'],
    '/path/to/Music': ['mp3', 'flac'],
    '/path/to/Pictures': ['jpg', 'png', 'icns', 'gif'],
    '/path/to/Movies': ['mp4', 'mkv', 'avi', 'mpeg']
}

for path_to_destination, extensions in my_dict.items():
    for ext in extensions:
        for file in glob.glob(path_to_source + '*.' + ext):
            print(file)
            shutil.move(file, path_to_destination)
