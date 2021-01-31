import tweepy
import time

auth = tweepy.OAuthHandler('TotXqAv831i0ftorsbKgaXgaM', 'hTOa1EVzF9Vn5jDTEYjbNICEyIDRgmCmnWaNqIktmMpdHcc0CP')
auth.set_access_token('1355721398954541061-mUYvAOv17pPaeID26LperN4f48ZiYy', '3xozyfGh3RtAEy9LGXC8tlOllBLMFZDHuUefOLbhidhz9')

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)


search_string = 'Python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersOfTweets):
	tweet.favorite()
	print('I liked it!')


#generous bot
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
# 	if follower == 'Bhavin':
# 		follower.follow()
# 		break