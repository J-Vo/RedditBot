import praw
import logging
import time

class Worker:
    def __init__(self, post_limit, comment_limit, subreddit):
        try:
            self.post_limit = post_limit
            self.comment_limit = comment_limit
            self.subreddit = subreddit

            logging.info('Worker created successfully')
        except:
            logging.error('Worker failed to be created.')

    def defaultTaskStart(self):

        reddit = praw.Reddit(client_id='rrSEOyLkRt_iCg',
                             client_secret="K9OEkUY2oFHGsiQwddDgMpZPEyY", password='GloriousPCMR5',
                             user_agent='testBot by u/Jocavo', username='Jocavo')

        POST_LIMIT = self.post_limit
        COMMENT_LIMIT = self.comment_limit
        SUBREDDIT_TO_SCAN = self.subreddit

        subreddit = reddit.subreddit(SUBREDDIT_TO_SCAN)

        logging.info('Worker starting scan.')

        for submission in subreddit.hot(limit=POST_LIMIT):
            print("Original Poster:", submission.author)

            #check if author has already been recorded

            #if no continue, if yes then skip next for loop.

            for comment in reddit.redditor(str(submission.author)).comments.new(limit=COMMENT_LIMIT):
                sub = reddit.comment(comment.id)

                print(sub.subreddit)
    def checkTasks(self):


    def sleepWorker(self, time):
        logging.info('Worker has been put to sleep for ', time, ' seconds.')
        time.sleep(time)

    def __del__(self):
        logging.info('Destructor called, worker deleted.')


