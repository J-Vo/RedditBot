import praw
import logging
import traceback
import sys
from dataHandler import DataHandler
import datetime

class Worker:
    def __init__(self, post_limit, comment_limit, subreddit,search_by_condition):
        try:
            self.post_limit = post_limit
            self.comment_limit = comment_limit
            self.subreddit = subreddit
            self.search_by_condition = search_by_condition
            logging.info('Worker created successfully %s', str(datetime.datetime.now()))
            client = DataHandler.initialize_data_handler()
            self.defaultTaskStart(client)
        except:
            logging.error('Worker failed to be created.', traceback.print_exc(file=sys.stdout))

    def defaultTaskStart(self, client):
        reddit = praw.Reddit(client_id='rrSEOyLkRt_iCg',
                             client_secret="K9OEkUY2oFHGsiQwddDgMpZPEyY", password='GloriousPCMR5',
                             user_agent='testBot by u/Jocavo', username='Jocavo')

        POST_LIMIT = self.post_limit
        COMMENT_LIMIT = self.comment_limit
        SUBREDDIT_TO_SCAN = self.subreddit
        SEARCH_BY_CONDITION = self.search_by_condition

        subreddit = reddit.subreddit(SUBREDDIT_TO_SCAN)
        logging.info('Worker starting scan.')
        for submission in subreddit.hot(limit=POST_LIMIT):
            reddit_user = str(submission.author)
            logging.info('Original Poster: %s ',reddit_user)
            if client.user_exists(reddit_user):
                logging.info('%s already exists.',reddit_user)
            else:
                client.insert_into_table(client.db_string,client.reddit_users_col_string,reddit_user)
                for comment in reddit.redditor(reddit_user).comments.new(limit=COMMENT_LIMIT):
                    sub = reddit.comment(comment.id)
                    client.insert_into_commment_history(sub)
                    logging.info(sub.subreddit)

    def sleepWorker(self, time):
        logging.info('Worker has been put to sleep for ', time, ' seconds.')
        time.sleep(time)

    def __del__(self):
        logging.info('Destructor called, worker deleted.')


