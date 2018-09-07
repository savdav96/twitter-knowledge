from models.IBMWatson.IBMWatsonClient import IBMWatsonClient

class IBMWatsonController:

    def __init__(self):
        self.response = None
        self.__client = IBMWatsonClient()
        self.relation = None

    def ask_ibm_watson(self, query, id):
        self.__client.watson_request(query)
        self.response = self.__client.get_response()
        if not (not self.response["intents"]):
            self.relation = {'Relation': self.response['intents'],
                             'Entities involved': self.response['entities'],
                             'Tweet text': query,
                             'Tweet id': id,
                             'Test result': "not validated"}
        else:
            self.relation = {'Relation': "not found",
                             'Entities involved': self.response['entities'],
                             'Tweet text': query,
                             'Tweet id': id,
                             'Test result': "not validated"}

    def print_response(self):
        print(self.response['intents'])
        print(self.response['entities'])

    def get_response(self):
        return self.response

    def get_last_relation_found(self):
        return self.relation



if __name__=="__main__":

    ic = IBMWatsonController()
    ic.ask_ibm_watson("A new version of fortnite will be dropped tomorrow")
    ic.print_response()
