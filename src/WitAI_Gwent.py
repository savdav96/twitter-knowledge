# python 2.7
# Funziona solo con frasi che parlano dello scontro tra fazioni con il verbo to face.
# Fazioni: Northern Realms, Nilfgaard, Scoia'tael, Monsters, Skellige
# Con frasi minime evidenzia sotto la voce entity le fazioni, e sott la voce relation il verbo

import urllib3
import certifi
import json

def convertTohttp(query):
    k=0
    for i in query:
        if query[k] == ' ':
            query = query[0:k]+"%20"+query[k+1:len(query)+1]

        k += 1
    result = "https://api.wit.ai/message?v=20170307&q=" + query
    return result


j = 1
while j != 0:
    q = input("Chiedi a Wit.AI:")
    q = convertTohttp(q)
    print(q)
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET', q, headers={'Authorization': 'Bearer HVRIVMJNL3SEGWJYFXM7S7KYNUNMYD35'})
    print(r.status)
    print(json.loads(r.data.decode('utf-8')))
