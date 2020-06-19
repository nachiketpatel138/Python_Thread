from threading import Thread,Event
import time

# by default value is False
# but we can change the value use 
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def light_switch():
    time.sleep(2)
    print('Light Green')
    e.set()                  # Value is true
    time.sleep(5)
    e.clear()               # Value is false
    print('Light Red')



def signal():
    e.wait()                # change the value either True or False
    while e.isSet():        #method isSet = 
        print('You Can Go....')
        time.sleep(1)
    print("done......")

e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=signal)
t1.start()
t2.start()