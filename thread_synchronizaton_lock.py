from threading import Thread,currentThread
from threading import *

# lock and acqure method
class Flight:
    def __init__(self,ava_seat):
        self.ava_seat = ava_seat
        self.l=Lock()
    def reserve(self,need_seat):
        self.l.acquire(blocking=True)
        print('Available seat :',self.ava_seat)
        if(self.ava_seat >=need_seat):
            name=currentThread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.ava_seat -= need_seat
            

        else:
            name=currentThread().name
            print(f"sorry !! {name}")
        self.l.release()
f=Flight(2)
t1=Thread(target=f.reserve,args=(1,),name='rahul')
t2=Thread(target=f.reserve,args=(1,),name='raj')
t3=Thread(target=f.reserve,args=(1,),name='raj1')
t4=Thread(target=f.reserve,args=(1,),name='raj2')

t4.start()
t1.start()
t2.start()
t3.start()