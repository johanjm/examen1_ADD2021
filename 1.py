
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = ""
csecret = ""
atoken = ""
asecret = ""
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
