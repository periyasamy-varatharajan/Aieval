import logging
log = logging.getLogger(__name__)
class Chat:
    def __init__(self,agent):
        self.agent = agent
        self.contents =[]
    def sendcontents(self):
        log.info(self.contents)
        response = self.agent.prompt(self.contents)
        self.addmessage("model",response)
        return response
    def addmessage(self,role,content):
        self.contents.append({"role": role, "parts": [{"text": content}]})
    def chitchat(self):
        message = ""
        print("say something")
        while(message!="exit"):
            message = input()
            self.addmessage("user",message)
            response = self.sendcontents()
            print(response)
            self.addmessage("model",response)
if __name__ == "__main__":
    chat = Chat()
    chat.chitchat()
    