import instaloader
L = instaloader.Instaloader()
username = ""  # write your username between the quotation marks
password = ""  # write your password between the quotation marks
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)
follow_list = []
follower_list = []
people_not_following_you_back = []

for followe in profile.get_followees():  # adding the people's username that you are following into a list
    follow_list.append(followe.username)

for follower in profile.get_followers():  # adding the people's username that are following you into a list
    follower_list.append(follower.username)


for followe in follow_list:  # adding the people's username that are not following you back into a list
    if not followe in follower_list:
        people_not_following_you_back.append(followe)

print("People that are not following you back: ")  # printing output to the console
for entity in people_not_following_you_back:
    print(entity)
