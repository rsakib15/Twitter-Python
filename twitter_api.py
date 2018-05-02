import tweepy


def get_api():
    config = {}
    execfile("config.py", config)
    cfg = {
        "consumer_key": config['consumer_key'],
        "consumer_secret": config['consumer_secret'],
        "access_token": config['access_token'],
        "access_token_secret": config['access_token_secret']
    }
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    auth.secure = True
    return tweepy.API(auth)

