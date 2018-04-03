# puoi usare questo main per i test delle classi

from src.WitAIClient import *
import json

client = WitAIClient('HVRIVMJNL3SEGWJYFXM7S7KYNUNMYD35')
client.wit_ai_request('Nilfgaard faces Skellige')
print(client.get_response())


#print(json.loads(client.get_response().decode('utf-8'), indent=4))