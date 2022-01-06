import urllib.request
import json

base_url = 'https://api.github.com/users/'


# def get_user_list(*args, url):
#     with urllib.request.urlopen(url) as response:
#         users = json.loads(response.read().decode())
#         for user in users:
#             user_list += [user['login']]
#         return user_list


# Get list of followers
def get_followers(userid):
    i = 1
    user_list = []

    while True:
        try:
            url = base_url + userid + '/followers?per_page=100&page=' + str(i)
            with urllib.request.urlopen(url) as response:
                users = json.loads(response.read().decode())
                if users:
                    for user in users:
                        user_list += [user['login']]
                elif not users:
                    break
        except:
            break
        i += 1
    return user_list


# Get list of following
def get_following(userid):
    i = 1
    user_list = []

    while True:
        try:
            url = base_url + userid + '/following?per_page=100&page=' + str(i)
            with urllib.request.urlopen(url) as response:
                users = json.loads(response.read().decode())
                if users:
                    for user in users:
                        user_list += [user['login']]
                elif not users:
                    break
        except:
            break
        i += 1
    return user_list


if __name__ == '__main__':
    username = str(input("Enter your GitHub username: "))
    followers = get_followers(username)

    following = get_following(username)
    no_follow_back_users = list(set(following) - set(followers))
    fans = list(set(followers) - set(following))

    # Count total followers
    follower_count = 0
    for follower in followers:
        follower_count += 1
    print(f'followers:', follower_count)

    # Count total following
    following_count = 0
    for follow in following:
        following_count += 1
    print(f'following:', following_count)

    # Print no follow back users
    print(f'\nHere are the users not following you back:')
    for no_follow_back in no_follow_back_users:
        print(no_follow_back)

    # Print fans
    print(f'\n\nHere are your fans:')
    for fan in fans:
        print(fan)
