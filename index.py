
#response = requests.get("""
#https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=twitterapi&skip_status=true&include_user_entities=false
#""");



#curl -X GET -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAPUDJgEAAAAATFLBA1Wr2uJc99nRJO%2FjULsLUEw%3Dn7Fg2oAjncEDs6hJprp0UwkekIFq3Fiiu9IpDJ3SQLGRWXiWhG"  \
#"https://api.twitter.com/labs/2/tweets/1138505981460193280?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"

import authorize;
import requests;


params = {"cursor":-1, "screen_name":"RebeccaJuLiaw", "skip_status":"true", "include_user_entities":"false"}

oauth = authorize.authorize();

response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)


print("Response status: %s" % response.status_code)
print("Body: %s" % response.text)



