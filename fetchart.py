import eyed3
import os
from auth import auth
import argparse
import json

parser = argparse.ArgumentParser(description='Fetch album art for discogs')
parser.add_argument('-r', '--recursive', help='Fetch album art recursively for subfolders', required=False, action='store_true')
parser.add_argument('-p', '--path', help='Path of folder containing an album', required=False, default='.')
args = vars(parser.parse_args())

discogs = auth()

extensions = ('.mp3', '.m4a', '.wav')

if args['recursive']:
	for root, dirs, files in os.walk(args['path']):
		files = [f for f in files if not f[0] == '.' and f.endswith(extensions)]
		dirs[:] = [d for d in dirs if not d[0] == '.']
		for name in files:
			tag = eyed3.load(os.path.join(root, name))
			artist = tag.tag.artist
			release = tag.tag.album
		resp, content = discogs.client.request("https://api.discogs.com/database/search?release_title={0}&artist={1}".format(release, artist), headers={'User-Agent': discogs.user_agent})
		json_result = json.loads(content)
		resp, image = discogs.client.request(json_result['results'][0]['thumb'], headers={'User-Agent': discogs.user_agent})
		with open(os.path.join(root, 'folder.jpg'), 'w') as fh:
			fh.write(image)
else:
	files = os.listdir(args['path'])
	files = [f for f in files if f.endswith(extensions)]
	for name in files:
		tag = eyed3.load(args['path'] + "/" + name)
		artist = tag.tag.artist
		release = tag.tag.album
	resp, content = discogs.client.request("https://api.discogs.com/database/search?release_title={0}&artist={1}".format(release, artist), headers={'User-Agent': discogs.user_agent})
	json_result = json.loads(content)		
	resp, image = discogs.client.request(json_result['results'][0]['thumb'], headers={'User-Agent': discogs.user_agent})
	with open(args['path'] + '/folder.jpg', 'w') as fh:
		fh.write(image)	



