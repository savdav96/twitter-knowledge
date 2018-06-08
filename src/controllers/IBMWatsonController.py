from models.IBMWatson.IBMWatsonClient import IBMWatsonClient

class IBMWatsonController:

    def __init__(self, relations):
        self.response = None
        self.__client = IBMWatsonClient()
        self.relations = relations

    def ask_ibm_watson(self, query):
        self.__client.watson_request(query)
        self.response = self.__client.get_response()
        if not (not self.response["intents"]):
            relation = {'Relation': self.response['intents'],
                        'Entities involved': self.response['entities'],
                        'Tweet text': query}
            self.relations.append(relation)

    def print_response(self):
        # TODO implement list of multiple requests and responses
        print(self.response['intents'])
        print(self.response['entities'])

    def get_response(self):
        return self.response


if __name__=="__main__":

    ic = IBMWatsonController()
    ic.ask_ibm_watson("A new version of fortnite will be dropped tomorrow")
    ic.print_response()
