
import authorize
import requests
import investor_filters
import json
import test_api
import time



oauth = authorize.authorize()


screen_name = input('Enter Screen Name: ')

#screen_name = "tferriss"
params = {"cursor":-1, "screen_name":screen_name, "skip_status":"true", "include_user_entities":"false", "count":200}

response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)
json_response = response.json() #test_api.tim_ferris()

#print(json_response)

print("Response status: %s" % response.status_code)
#print("Body: %s" % response.json()) # response.text also exists

next_cursor = json_response["next_cursor"] # to get next page do another api call using this cursor

# get all users with "investor" in their description

investors = investor_filters.get_investors(json_response["users"])

while (next_cursor != 0):
    print(next_cursor)
    params["cursor"] = next_cursor
    response = oauth.get("https://api.twitter.com/1.1/friends/list.json", params = params)
    print("Response status: %s" % response.status_code)
    if response.status_code != 200:
        print(response.text)
    json_response = response.json()
    next_cursor = json_response["next_cursor"]
    investors.extend(investor_filters.get_investors(json_response["users"]))
    time.sleep(61)

f = open("./investors.csv", "x")
for i in range(len(investors)):
    #print(investors[i])
    #print('\n')
    investors[i]["description"] = investors[i]["description"].replace(',','')
    f.write(investors[i]["screen_name"] + ',' + "\"" + investors[i]["description"] + "\"" + '\n')

f.close()


