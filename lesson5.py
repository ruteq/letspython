from os import walk
#from pil import Image
#import re



for d, dirs, files in walk('d:\Python'):
	for f in files:
		print (f)