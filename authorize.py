
import apikeys
import os
from requests_oauthlib import OAuth1Session

def authorize():
    keys = apikeys.get_keys()
    consumer_key = keys["api"]  # Add your API key here
    consumer_secret = keys["apisecret"]  # Add your API secret key here

    # Get request token
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    print("Got OAuth token: %s" % resource_owner_key)

    # # Get authorization
    base_authorization_url = 'https://api.twitter.com/oauth/authorize'
    authorization_url = oauth.authorization_url(base_authorization_url)
    print('Please go here and authorize: %s' % authorization_url)
    verifier = input('Paste the PIN here: ')

    # # Get the access token
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    oauth = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=resource_owner_key,
                        resource_owner_secret=resource_owner_secret,
                        verifier=verifier)
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens['oauth_token']
    access_token_secret = oauth_tokens['oauth_token_secret']

    # Make the request
    oauth = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

    return oauth
    