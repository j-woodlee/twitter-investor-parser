
import authorize;
import requests;
import investor_filters;


oauth = authorize.authorize();


#screen_name = input('Enter Screen Name: ')

screen_name = "tferriss"
params = {"cursor":-1, "screen_name":screen_name, "skip_status":"true", "include_user_entities":"false", "count":10}

response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)
json_response = response.json()

print("Response status: %s" % response.status_code)
#print("Body: %s" % response.json()) # response.text also exists

print("\n\n\n\n\n\n\n\n\n\n")

next_cursor = json_response["next_cursor"]; # to get next page do another api call using this cursor


#print(json_response["users"])
#print("\n\n\n\n\n\n\n\n\n\n")

# get all users with "investor" in their description
users = investor_filters.get_investors(json_response["users"])

#print(users);

#while (next_cursor != 0):



