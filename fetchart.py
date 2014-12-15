import eyed3
import sys
import os
from auth import auth
import urlparse
import oauth2 as oauth

discogs = auth()

resp, content = discogs.client.request("https://api.discogs.com/images/R-40522-1098545214.jpg", headers={'User-Agent': discogs.user_agent})

with open('folder.jpg', 'w') as fh:
	fh.write(content)



