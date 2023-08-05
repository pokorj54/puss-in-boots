import praw
import my_secret_token

def open_reddit():
    reddit_credentials=my_secret_token.get_reddit_credentials()

    reddit = praw.Reddit(
        client_id=reddit_credentials[0],
        client_secret=reddit_credentials[1],
        user_agent="Puss in boots by u/Cenislav",
    )
    return reddit
