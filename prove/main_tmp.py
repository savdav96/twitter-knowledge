
from src.IBMWatsonClient import IBMWatsonClient
from src.WitAIClient import *
import json

#*client = WitAIClient('HVRIVMJNL3SEGWJYFXM7S7KYNUNMYD35')
#client.wit_ai_request('Nilfgaard faces Skellige')
#print(client.get_response())
#print(json.loads(client.get_response().decode('utf-8'), indent=4))

client = IBMWatsonClient()
client.watson_request('Red Dead Redemption 2 will be released on October 2018')
print(client.get_response())
