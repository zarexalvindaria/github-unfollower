import urllib.request
import json


def get_user_list(url):
    with urllib.request.urlopen(url) as response:
        users = json.loads(response.read().decode())
        user_list = []
        for user in users:
            user_list += [user['login']]
        return user_list


# Get list of followers
def get_followers(userid):
    return get_user_list('https://api.github.com/users/' + userid + '/followers')


# Get list of following
def get_following(userid):
    return get_user_list('https://api.github.com/users/' + userid + '/following')


if __name__ == '__main__':
    username = str(input("Enter your GitHub username: "))
    followers = get_followers(username)
    following = get_following(username)
    not_following_users = list(set(following) - set(followers))
    print(f'\nHere are the users not following you:')
    for user_to_unfollow in not_following_users:
        print(user_to_unfollow)
