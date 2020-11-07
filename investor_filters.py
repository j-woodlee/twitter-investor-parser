def get_investors(users):
    # users is a list of user objects(dictionaries) as defined by twitter API 1.1
    ret_users = []

    for user in users:
        # print(user["description"])

        if (user["description"].find("investor") != -1):
            ret_users.append(user)
            #print("user added: ")
            # print(user)
            # print("\n\n")

    return ret_users