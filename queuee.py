from collections import deque
import time
import threading



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
    
    def placeOrd(self, order):
        #print(order)
        for i in order:
            time.sleep(0.5)
            self.enqueu(i)
            #print(self.queue)
            print(f"Order {i} has started!")

    def finishOrd(self):
        time.sleep(1)
        while True:
            order = self.dequeue()
            print("Now serving: ",order)
            time.sleep(2)
        # time.sleep(2.0)
        # for j in self.queue:
        #     print(len(j))
        #     #self.dequeue()
        #     #print(f"Order {self.queue} has finished.")
    





q = Queuee()
orders = ['pizza','samosa','pasta','biryani','burger']


# q.enqueu(15)
# q.enqueu(25)
# q.enqueu(35)
# q.enqueu(45)
# q.enqueu(55)
#print(q.length())
#print(q.queue)

#q.dequeue()
#print(q.length())

#print(q.placeOrd(["ham", "Turk", "chick"]))

#print(q.queue)

po = threading.Thread(target=q.placeOrd,args=(orders,))
go = threading.Thread(target=q.finishOrd)

po.start()
go.start()

po.join()
go.join()

#print(f"PO : {po} , Finished : {go}")