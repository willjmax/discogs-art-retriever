import eyed3
import os
from auth import auth
import urlparse
import oauth2 as oauth
import argparse

parser = argparse.ArgumentParser(description='Fetch album art for discogs')
parser.add_argument('-r', '--recursive', help='Fetch album art recursively for subfolders', required=False, action='store_true')
parser.add_argument('-p', '--path', help='Path of folder containing an album', required=False, default='.')
args = vars(parser.parse_args())

#discogs = auth()

extensions = ('.mp3', '.m4a', '.wav')

for root, dirs, files in os.walk(args['path']):
	files = [f for f in files if not f[0] == '.' and f.endswith(extensions)]
	dirs[:] = [d for d in dirs if not d[0] == '.']
	for name in files:
		print (os.path.join(root, name))
	for name in dirs:
		print (os.path.join(root, name))


'''
resp, content = discogs.client.request("https://api.discogs.com/images/R-40522-1098545214.jpg", headers={'User-Agent': discogs.user_agent})

with open('folder.jpg', 'w') as fh:
	fh.write(content)
'''




