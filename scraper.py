import praw
from praw.models import MoreComments


def get_data(subreddit_name):

    dataArr = []
    commentArr = []
    reddit = praw.Reddit(client_id="YOUR_ID",
                         client_secret="YOUR_SECRET",
                         password="YOUR_EMAIL_PASSWORD",
                         user_agent="NAME_OF_THE_APP",
                         username="REDDIT_USERNAME")

    subreddit = reddit.subreddit(subreddit_name)
    members = subreddit.subscribers
    activeUsers = subreddit.active_user_count
    for submission in subreddit.new(limit=100):

        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            for comment in submission.comments:
                if isinstance(comment, MoreComments):
                    continue
                commentArr.append(comment.body)

            data = {
                "title": submission.title,
                "url": url,
                "comments": commentArr
            }
            dataArr.append(data)
            # print(commentArr)

            commentArr = []

    return members, activeUsers, dataArr
