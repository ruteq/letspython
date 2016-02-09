import Image, os

for path, dirs, files in os.walk('D:\Python_pics'):
    for _file in files:
        try:
            im = Image.open(os.path.join(path, _file))
            im.resize([x / 2 for x in im.size]).save(os.path.join(path, 'resized_' + _file))
            print('{}'.format(_file))
        except IOError:
            continue