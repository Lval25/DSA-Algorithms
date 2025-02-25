from collections import deque



#First in First out


class Queuee:
    def __init__(self):
        self.queue = deque()
    

    def enqueu(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == 0
    
    def length(self):
        return len(self.queue)
    


q = Queuee()

q.enqueu(15)
q.enqueu(25)
q.enqueu(35)
q.enqueu(45)
q.enqueu(55)
print(q.length())
print(q.queue)

q.dequeue()
print(q.length())