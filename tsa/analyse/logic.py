import tweepy
from textblob import TextBlob
import pandas

def logicBox(query):
    consumer_key = 'f6Ei7G3NG4b313deOmXxMQmzO'
    consumer_secret = 'cSjZa4OpaJiYBLwAYdCnHuxIXJQ9eTfpb9XqlOD54WtxrdHdlZ'

    access_token = '724283351192899584-NoNK2PyFelNFCLrykH6ju9zY2q6rh49'
    access_token_secret = 'eZ8z951uSGtfZPkfR5qffHbx7m4dW7nfUGxrmUh9jAjf9'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    public_tweets = tweepy.Cursor(api.search, query ,tweet_mode='extended').items(100)

    li = []
    p = 0
    n = 0
    neu = 0

    for tweets in public_tweets:
        try:
            if 'retweeted_status' in tweets._json:
                tweets = (tweets._json['retweeted_status']['full_text'])
            else:
                tweets = (tweets.full_text)
        except:
            pass

        li.append(tweets)
        analysis = TextBlob(tweets)
        senti = analysis.sentiment.polarity
        if senti>0:
            p += 1
        elif senti==0:
            neu += 1
        elif senti<0:
            n += 1

    df = pandas.DataFrame(data=li)
    writer = pandas.ExcelWriter("C:/Users/Ria/Desktop/DS_Prac_Pycharmfiles/tsa/analyse/static/analyse/TweetFile.xlsx")
    df.to_excel(writer,sheet_name='Sheet1')
    writer.save()
    writer.close()
    return [li,p,neu,n]