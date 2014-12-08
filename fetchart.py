import discogs_client
import eyed3
import sys
import os
import keys
from pprint import pprint

#auth.authenticate()

discogs = discogs_client.Client("Album Art Fetcher")
discogs.set_consumer_key(keys.consumer_key, keys.consumer_secret)
auth_url = discogs.get_authorize_url()
print "Verify at " + auth_url[2]
oauth_verifier = raw_input("Verification code: ")
discogs.get_access_token(oauth_verifier)
results = discogs.search("Pulse Demon", type="release")
id = results[0].id
release = discogs.master(id)
print release.images


'''
filetypes = [".mp3", ".wav", ".flac", ".m4a"]

path = sys.argv[1]
if not os.path.isdir(path):
	print "Invalid path"
	exit()

files = os.listdir(path)
for filetype in filetypes:
	if files[2].endswith(filetype):
		track = eyed3.load(path + "/" + files[2])
		tag = track.tag
		album = tag.album
		artist = tag.artist
'''
