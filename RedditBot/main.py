import praw

reddit = praw.Reddit(client_id='rrSEOyLkRt_iCg',
                     client_secret="K9OEkUY2oFHGsiQwddDgMpZPEyY", password='GloriousPCMR5',
                     user_agent='testBot by u/Jocavo', username='Jocavo')


subreddit = reddit.subreddit('all')

for submission in subreddit.hot(limit=2):
    print(submission.author)

    user = submission.author

    print(user.comment_karma)

    subscribed = list(reddit.user.subreddits(limit=None))

    print(subscribed)

