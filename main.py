import datetime
import time
import tweepy
import creds
import mybday

# OAuth Handler
auth = tweepy.OAuthHandler(
    creds.consumer_key,
    creds.consumer_secret
)
auth.set_access_token(
    creds.access_token,
    creds.access_token_secret
)
api = tweepy.API(
    auth,
    wait_on_rate_limit=True
)


# Rate Limit Handler
def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.TooManyRequests:
            time.sleep(15 * 60)


# Verify Twitter API Credentials #
def verify_creds():
    try:
        api.verify_credentials()
        print('Authentication OK')
    except tweepy.errors.TweepyException:
        print('Error during authentication')


# Date Variables
class myBirthday:
    def __init__(self):
        # Date object variables
        self.today = datetime.date.today().strftime("%b" + "%d")
        self.birthday = mybday.date


bday = myBirthday()


# Compare today's date with birthday variable
def check_date():
    try:
        birthday = bday.today == bday.birthday
        return birthday
    except:
        print('Program encountered an unexpected error')


def post_msg():
    if check_date():
        print('Posting your birthday message to Twitter...\n')
        with open('lyrics.txt', 'r') as lyrics:
            api.update_status("Custom message goes here...\n\n" + lyrics.read())
        print('Your Twitter status has been successfully updated...\n\tHappy Birthday!')
    else:
        print("It's not your birthday yet, dweeb!\n\tCheck back another time.")


post_msg()
