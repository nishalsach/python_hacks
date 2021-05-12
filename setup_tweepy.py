def setup_tweepy():
    access_token = "2444159130-ASPMSfdrthFAuK2dUZjj9ziaG7rO9c1vrXwnmzB"
    access_token_secret = "FeSmEpxesLUHIhv3pH9DvzDywrmmUFyO7xyk6ufbJP3qK"
    consumer_key = "IuQLHdZtaVoquJeTLiaaCsfVs"
    consumer_secret = "RC5Y1Omr9VCTSxg4lGjPrWJrFUXxLmrkSfr1TjTt1CnAn2gFuh"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,timeout=1200)
    return api

def make_directory(directory_path):
    try:
        os.mkdir(directory_path)
        print(directory_path)
    except FileExistsError:
        pass