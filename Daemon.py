from threading import Thread,currentThread
from time import sleep

def teacher():
    for i in range(1,11):
        # sleep()
        print("teaching Session : ",i)
        pass

t1=Thread(target=teacher)
t1.setDaemon(True)
t1.start()
t1.join()
print("Exam over",currentThread().getName())