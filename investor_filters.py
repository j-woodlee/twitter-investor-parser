def get_investors(users):
    # users is a list of user objects(dictionaries) as defined by twitter API 1.1
    ret_users = []

    for user in users:
        if (user["description"].find("invest") != -1):
            ret_users.append(user)
            #print("user added: ")
            # print(user)
            # print("\n\n")

    return ret_users


def dms_open(users):
    ret_users = []

    for user in users:
        if (user["description"].find("invest") != -1):
            ret_users.append(user)
            #print("user added: ")
            # print(user)
            # print("\n\n")

    return ret_users
