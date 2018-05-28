from models.IBMWatson.IBMWatsonClient import IBMWatsonClient


class IBMWatsonController:

    def __init__(self):
        self.response = []
        self.__client = IBMWatsonClient()

    def ask_ibm_watson(self, query):
        self.__client.watson_request(query)
        self.response.append(self.__client.get_response())

    def print_response(self):
        # TODO implement list of multiple requests and responses
        print(self.response[0]['intents'])
        print(self.response[0]['entities'])


if __name__=="__main__":

    ic = IBMWatsonController()
    ic.ask_ibm_watson("A new version of fortnite will be dropped tomorrow")
    ic.print_response()
