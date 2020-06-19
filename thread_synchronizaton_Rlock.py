from threading import *

class Flight:
    def __init__(self,ava_seat):
        self.ava_seat = ava_seat
        self.l=RLock()       # RLock # we simple use RLoc only
        print(self.l)
    def reseve(self,need_seat):
        self.l.acquire()
        self.l.acquire()

        print(self.l)

        # print(f'avalable seat are {self.ava_seat}')
        if(self.ava_seat>=need_seat):
            name=current_thread().name
            # print(f'{need_seat} is alloted {name}')
            self.ava_seat-=need_seat
        
        else:
            name=current_thread().name
            # print(f'Sorry')
        self.l.release()
        self.l.release()
    
        print(self.l)

f=Flight(2)
t1=Thread(target=f.reseve,args=(1,),name='raj1')
t2=Thread(target=f.reseve,args=(1,),name='raj2')
t3=Thread(target=f.reseve,args=(1,),name='raj3')
t1.start()
t2.start()
t3.start()

