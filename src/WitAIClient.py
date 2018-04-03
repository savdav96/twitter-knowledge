import urllib3
import json
import certifi


class WitAIClient:

    def __init__(self, token):  # il costruttore richiede un token relativo ad un account su witAI
        self.token = token

    def convertTohttp(self, query): # converte una frase da sottoporre a witAI in richiesta http
        k = 0
        for i in query:
            if query[k] == ' ':
                query = query[0:k] + "%20" + query[k + 1:len(query) + 1]

            k += 1
        result = "https://api.wit.ai/message?v=20170307&q=" + query
        return result

    def message(self, text):    # invia una frase in una richiesta http a witAI e restituisce la risposta
        q = self.convertTohttp(text)
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        request = http.request('GET', q, headers={'Authorization': 'Bearer '+self.token})
        print('status code: ', end='')
        print(request.status)
        return json.loads(request.data.decode('utf-8'))

    def prettyPrint(self, d, indent=0): # stampa decentemente i dizionari (inutilizzata)
        for key, value in d.items():
            print('\t' * indent + str(key) + ":")
            if isinstance(value, dict):
                self.pretty(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))

