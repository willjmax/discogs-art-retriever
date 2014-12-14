import eyed3
import sys
import os
import auth
import urlparse
import oauth2 as oauth

client = auth.authenticate()

resp, content = client.request("https://api.discogs.com/images/R-40522-1098545214.jpg", headers={'User-Agent': user_agent})

with open('folder.jpg', 'w') as fh:
	fh.write(content)



