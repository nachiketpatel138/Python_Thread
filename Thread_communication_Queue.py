# Queue --> first in first out
from threading import Thread
from queue import Queue
import time

class Producer:
    def __init__(self):
        self.q=Queue()

    def producer(self):
        for i in range(1,6):
            print("item produce ",i)
            self.q.put(i)
            time.sleep(1)

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consumer(self):
        for i in range(1,6):
            print("item Consumed..", self.prod.q.get(i))

p=Producer()
c=Consumer(p)   





 
t1=Thread(target=p.producer)
t2=Thread(target=c.consumer)
t1.start()
t2.start()
