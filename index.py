
import authorize
import requests
import investor_filters
import json
import test_api



oauth = authorize.authorize()


#screen_name = input('Enter Screen Name: ')

screen_name = "tferriss"
params = {"cursor":-1, "screen_name":screen_name, "skip_status":"true", "include_user_entities":"false", "count":50}

response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)
json_response = response.json() #test_api.tim_ferris() #

print(json_response)

#print("Response status: %s" % response.status_code)
#print("Body: %s" % response.json()) # response.text also exists

#print("\n\n\n\n\n\n\n\n\n\n")

next_cursor = json_response["next_cursor"] # to get next page do another api call using this cursor

print("\n\n\n\n\n\n\n\n\n\n")
#print(json_response["users"])


# get all users with "investor" in their description

investors = investor_filters.get_investors(json_response["users"])

print("\n\n\n\n\n\n\n\n\n\n")

# for investor in investors:
#     print(investor["description"])
#     print("\n")

#while (next_cursor != 0):
    print(next_cursor)
    params["cursor"] = next_cursor
    response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)
    json_response = response.json()
    next_cursor = json_response["next_cursor"]
    investors.append(investor_filters.get_investors(json_response["users"]))



for investor in investors:
    print(investor["description"])
    print("\n")


