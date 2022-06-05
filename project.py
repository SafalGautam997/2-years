import praw
import datetime
reddit = praw.Reddit(client_id="145RKY8csM8D0JfqTz6k5Q",
                     client_secret="jQboL3Gmb_k7hnivXou2FmiSHGdfaQ",
                     user_agent="hewhoremained",
                     username="Melodic_Parsnip_42",
                     password="safalGautam@1")
subred = reddit.subreddit("PewdiepieSubmissions")
hot = subred.hot(limit = 10)
new = subred.new(limit = 10)
top = subred.top(limit = 10)
type(top)
x = next(top)
dir(x)
for i in top:
    print(i.author.name,
          i.title,
          i.ups,
          i.downs,
          i.url,
          datetime.datetime.utcfromtimestamp(i.created_utc))
list1 = []
