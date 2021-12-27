import urllib.request
import json

base_url = 'https://api.github.com/users/'


def get_user_list(url):
    with urllib.request.urlopen(url) as response:
        users = json.loads(response.read().decode())
        user_list = []
        for user in users:
            user_list += [user['login']]
        return user_list


# Get list of followers
def get_followers(userid):
    return get_user_list(base_url + userid + '/followers')


# Get list of following
def get_following(userid):
    return get_user_list(base_url + userid + '/following')


if __name__ == '__main__':
    username = str(input("Enter your GitHub username: "))
    followers = get_followers(username)
    following = get_following(username)
    no_follow_back_users = list(set(following) - set(followers))
    print(f'\nHere are the users not following you back:')
    for no_follow_back_user in no_follow_back_users:
        print(no_follow_back_users)
