import oauth2 as oauth
import urlparse
import keys

def authenticate():
	request_token_url = "https://api.discogs.com/oauth/request_token"
	authorize_url = "https://www.discogs.com/oauth/authorize"
	access_token_url = "https://api.discogs.com/oauth/access_token"
	user_agent = "Album Art Fetcher"

	consumer = oauth.Consumer(keys.consumer_key, keys.consumer_secret)
	client = oauth.Client(consumer)

	resp, content = client.request(request_token_url, "POST", headers={"User-Agent": user_agent})

	if resp['status'] != '200':
		sys.exit('Invalid Response {0}.'.format(resp['status']))

	request_token = dict(urlparse.parse_qsl(content))

	accepted = 'n'
	while accepted.lower() == 'n':
		print
		accepted = raw_input('Have you authorized me at {0}?oauth_token={1} [y/n] :'.format(authorize_url, request_token['oauth_token']))

	oauth_verifier = raw_input('Verification code: ')

	token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST", headers={'User-Agent': user_agent})
	access_token = dict(urlparse.parse_qsl(content))

	token = oauth.Token(key=access_token['oauth_token'], secret=access_token['oauth_token_secret'])
	client = oauth.Client(consumer, token)

	return client
