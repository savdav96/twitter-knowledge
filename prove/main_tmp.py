
from src.IBMWatsonClient import IBMWatsonClient
import json

#IBM Watson Assistant limita le richieste a 10 000 al mese

client = IBMWatsonClient()
client.watson_request('All the Marvel movies ranked from cringiest to pretty damn good')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
print("-----------------------------------------------------------------------------------")
client.watson_request('Even more PSN games are on sale now until May 29')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
print("-----------------------------------------------------------------------------------")
client.watson_request('Our review of Avengers: InfinityWar!!')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))
print("-----------------------------------------------------------------------------------")
client.watson_request('The first teaser trailer for Avengers : InfinityWar showed off SpiderMan')
print(json.dumps(client.get_response(), sort_keys=True, indent=4))

