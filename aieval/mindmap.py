import logging
import json
import random
log = logging.getLogger(__name__)


class Mindmap:
    def __init__(self,agent):
        self.initques()
        log.info("question loaded")
        self.threshold = 5
        self.agent = agent
    def initques(self):
        with open("questions_set.json","r") as qfile:
            queslist = json.load(qfile)
            self.questions = dict()
            for i in queslist:
                self.questions[i["id"]] = i
                self.questions[i["id"]]["score"]=-1

    def shootques(self,qid):
        log.info("asking question",qid)
        score = random.randint(1,10)
        log.info("got score"+str(score))
        return score

    def traversequestion(self):
        queue = random.sample(sorted(self.questions),5)
        #update initial question section
        #work out on eliminatin startegy
        while(queue):
            current = queue[0]
            print(current)
            score = self.shootques(self.questions[current])
            self.questions[current]["score"]=score
            if score>self.threshold:
                log.info("crossed threshold")
                log.info("neighbours"+str(self.questions[current]["neighbors"]))
                for i in self.questions[current]["neighbors"]:
                    if i not in queue and self.questions[i]["score"]==-1:
                        queue.append(i)
            queue.pop(0)
        