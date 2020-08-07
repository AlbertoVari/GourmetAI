import time
import tweepy
auth = tweepy.OAuthHandler("MoHU91iJZEEull5B07ZICb7T2", "nZUAZ5jXkqurrnlL2TsCVaFWKrQjC5nv2TP2WqolZQ23AHtCcS")
auth.set_access_token("722170107171090433-JBLTI5I61nq53a4x9hKzcjBmRU1Axg0", "VThOiix7pe3dvKwINKTFYhTONF6idyTSqL2jTpBt7pxpn")

api = tweepy.API(auth,wait_on_rate_limit=True)

user = api.get_user("albertovari")

sleeptime = 4
pages = tweepy.Cursor(api.followers, screen_name="albertovari").pages()

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
         api.send_direct_message(user.id,"https://twitter.com/AlbertoVari/status/1291402267913052162?s=20")
         print(user.screen_name,user.id)

