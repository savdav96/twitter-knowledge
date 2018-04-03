import urllib.request
import json
import certifi


class WitAIClient:

    def __init__(self, token):
        self.response = None
        self.token = token

    def get_response(self):
        return self.response

    def wit_ai_request(self, q):

        url = _convert_to_url(q)
        header = {'Authorization': 'Bearer '+self.token}
        req = urllib.request.Request(url=url, headers=header, method='GET')
        res = urllib.request.urlopen(req)
        self.response = res.read()


def _convert_to_url(query):

    # Statica (non indentata in classe) in quanto non utilizza self

    index = 0
    while index < len(query):
        if query[index] == ' ':
            query = query[0:index] + "%20" + query[index + 1:len(query) + 1]
        index += 1

    result = "https://api.wit.ai/message?v=20170307&q=" + query
    return result


'''
    def prettyPrint(self, d, indent=0): # stampa decentemente i dizionari (inutilizzata)
        for key, value in d.items():
            print('\t' * indent + str(key) + ":")
            if isinstance(value, dict):
                self.pretty(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))
'''

### per la print userei il get_

#print('status code: ', end='')
# print(request.status)
# return json.loads(request.data.decode('utf-8'))