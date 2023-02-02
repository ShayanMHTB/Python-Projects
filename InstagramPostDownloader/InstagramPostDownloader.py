'''
	This is a script generated with OpenAI, which is supposed
	to get an instagrma username and download his/her posts.

	Eaxample:
		Input: python InstagramPostDownloader.py [USERNAME]
		Output: [USERNAME] posts downloaded to the local 
				machine in the same directory

'''

import requests
import json

def download_posts(username):
    # Get the user ID using the Instagram API
    response = requests.get(f'https://www.instagram.com/{username}/?__a=1')
    user_id = response.json()['graphql']['user']['id']

    # Use the user ID to get the user's posts
    response = requests.get(f'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables={{%22id%22%3A%22{user_id}%22%2C%22first%22%3A12%2C%22after%22%3A%22{end_cursor}%22}}')
    posts = response.json()['data']['user']['edge_owner_to_timeline_media']['edges']

    # Save the posts to a file
    with open(f'{username}_posts.json', 'w') as f:
        json.dump(posts, f)

    print(f'{len(posts)} posts downloaded for user {username}.')

if __name__ == '__main__':
    username = input('Enter a Instagram username: ')
    download_posts(username)
