import praw
import config
import re
import time

volunteering_regex_list = [
    r'Why don\'t we (.*)',
    r'(Someone|somebody) (should|needs to) (.*)',
    r'(Please )?(Can|Could) (someone|somebody) (.*)',
    r'It would be (good|nice|amazing|useful) if (.*)',
    r'(I think )?(that )?We should (.*)'
]

replied_to = []

def bot_init():
  bot = praw.Reddit(user_agent='VoluntoldBot developed by a real keyboard ninja v0.0.1',
                    client_id=config.REDDIT_ID,
                    client_secret=config.REDDIT_SECRET,
                    username=config.USERNAME,
                    password=config.PASSWORD)
  return bot;

def run_bot(bot, sub):
  subreddit = bot.subreddit(sub)
  comments = subreddit.stream.comments()

  for comment in comments:
    text = comment.body
    author = comment.author
    for regex in volunteering_regex_list:
      if re.search(regex,text, re.IGNORECASE):
        if comment.id not in replied_to:
          replied_to.append(comment.id)
          message = "Thank you, {0} for volunteering! Now go do it.".format(author)
          comment.reply(message)


bot = bot_init()
run_bot(bot, 'test')
time.sleep(1800)
