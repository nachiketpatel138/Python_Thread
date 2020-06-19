from threading import Thread,Condition
from time import sleep

# notify(n=1)--> this method is used to immediately wake up one thread waiting on the condition.where n is number of thread need to wake up (by default value is 1)

# notify_all()--> this metohd is used to wake up all threads waiting on the condition
# wait(Timeout=None)-->This method wait until notified or until a timeout occurs

lst=[]
def produce():
    cv.acquire()
    for i in range(1,6):
        lst.append(i)
        sleep(0.5)
        print("Item Produced...")

    cv.notify()
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)



cv=Condition()
t1=Thread(target=produce)
t2=Thread(target=consume)
t1.start()
t2.start()
