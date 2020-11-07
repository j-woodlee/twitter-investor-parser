
import authorize;
import requests;


params = {"cursor":-1, "screen_name":"RebeccaJuLiaw", "skip_status":"true", "include_user_entities":"false"}

oauth = authorize.authorize();

response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)


print("Response status: %s" % response.status_code)
print("Body: %s" % response.text)



