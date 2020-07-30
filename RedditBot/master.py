import logging
import praw
import time
from worker import Worker
class Master:
    @staticmethod
    def createWorker(post_limit, comment_limit, subreddit, search_by_condition):
        try:
            newWorker = Worker(post_limit, comment_limit, subreddit, search_by_condition)
            newWorker.defaultTaskStart()
            logging.info('Master has created worker.')
        except:
            logging.error('Master has failed to created worker.')
    #def createTask(self):