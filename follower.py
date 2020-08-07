import time
import tweepy
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth,wait_on_rate_limit=True)

user = api.get_user("")

sleeptime = 4
pages = tweepy.Cursor(api.followers, screen_name="").pages()

while True:
    try:
         page = next(pages)
         time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
         time.sleep(600)
         page = next(pages)
    except StopIteration:
          break
    for user in page:
         api.send_direct_message(user.id,"")
         print(user.screen_name,user.id)

