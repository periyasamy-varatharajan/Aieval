import logging
import json
import random
log = logging.getLogger(__name__)


class Mindmap:
    def __init__(self,chat):
        self.initques()
        log.info("question loaded")
        self.threshold = 5
        self.chat = chat
    def initques(self):
        with open("questions_set.json","r") as qfile:
            queslist = json.load(qfile)
            self.questions = dict()
            for i in queslist:
                self.questions[i["id"]] = i
                self.questions[i["id"]]["score"]=-1
    def initchat(self):
        self.chat.addmessage("user","you are interviewer you will be always give question answer pair rate the answer 1 to 10 for correctness and just respond in json score and a response should look you are directly talking to the candidate")

    def shootques(self,question):
        log.info("asking question",question)
        answer = input(question["question"])
        if answer.startswith("admin"):
            return int(answer.split(" ")[1])
        prompt = f"the candidate has been asked the question < {question} > and he given the reply < {answer} > "
        self.chat.addmessage("user",prompt)
        response = json.loads(self.chat.sendcontents())
        score = response["score"]
        print(response["response"])
        #score = random.randint(1,10)
        log.info("got score"+str(score))
        return score

    def traversequestion(self):
        self.initchat()
        queue = random.sample(sorted(self.questions),5)
        #update initial question section
        #work out on eliminatin startegy
        asked = []
        while(queue):
            current = queue[0]
            #print(current)
            score = self.shootques(self.questions[current])
            self.questions[current]["score"]=score
            if score>self.threshold:
                log.info("crossed threshold")
                log.info("neighbours"+str(self.questions[current]["neighbors"]))
                for i in self.questions[current]["neighbors"]:
                    if i not in queue and self.questions[i]["score"]==-1:
                        queue.append(i)
            asked.append(current)
            queue.pop(0)
        for i in asked:
            print(self.questions[i])