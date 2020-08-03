import logging
from master import Master
from worker import Worker
from dataHandler import DataHandler
import datetime

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info("Instantiating worker")

#post_limit = 5
#comment_limit = 5
#subreddit = "all"
#search_by_condition = "hot"

#Master.createWorker(post_limit, comment_limit, subreddit, search_by_condition)

dh = DataHandler.initialize_data_handler()

reddit_user = 'boomshiki'
pk = dh.get_reddit_user_pk(reddit_user)

print(pk)