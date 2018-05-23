from watson_developer_cloud import AssistantV1
import  json


class IBMWatsonClient:

    def __init__(self):
        self.watson_assistant = AssistantV1(
            username='c5bee141-5336-45fe-8334-0943daec826d',
            password='4YRkkDQatabE',
            version='2018-02-16',
        )
        self.response = None

    def get_response(self):
        return self.response

    def watson_request(self, q):
        self.response = self.watson_assistant.message(
            workspace_id='0bc1a302-74f5-44ff-991e-696495284c78',
            input={'text': q}
        )





