
from src.View import View
from src.IBMWatsonClient import IBMWatsonClient
import json
from src.FileIO import *

#IBM Watson Assistant limita le richieste a 10 000 al mese

list = []
save_obj(list, "twitter knowlegde data")
'''
client = IBMWatsonClient()
client.watson_request('All the Marvel movies ranked from cringiest to pretty damn good')
print(client.get_response()['intents'])
print(client.get_response()['entities'])
print("-----------------------------------------------------------------------------------")
client.watson_request('Even more PSN games are on sale now until May 29')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
print("-----------------------------------------------------------------------------------")
client.watson_request('Our review of Avengers: InfinityWar!!')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
print("-----------------------------------------------------------------------------------")
client.watson_request('The first teaser trailer for Avengers : InfinityWar showed off SpiderMan')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
'''

