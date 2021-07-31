
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "oeTUFI6aH0mux9p8bLJdcDaRt"
csecret = "hy9kVzxyZ3A5BrukvMOO2a1ZV2ZqkktpFqqR3dhXbPSrdLf4Xi"
atoken = "115946548-n0jFqRCg2aRLrWmWfEKK58P6OzQpHUEbVQloYWEu"
asecret = "YoPe97BHA9r9IZB2y4KMKjkaYPc562mOZJqQMsgF7pF8B"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:0712@127.0.0.1:5984')
try:
    db = server.create('twitter1')
except:
    db = server['twitter1']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-80.63,-3.23,-77.07,0.49])  
twitterStream.filter(track=['juegos2021'])
