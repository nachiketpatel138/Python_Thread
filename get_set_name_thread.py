from threading import Thread,currentThread
import threading
# currentThread().name = '1'
t= threading.current_thread().getName()
print(t)
# currentThread().name = '2'
g=threading.currentThread().getName()
print(g)
def dis():
    for i in range(5):
        # currentThread().setName('str1')
        currentThread().name = 'str2'
        # print('sub thread',currentThread().getName())

t=Thread(target=dis)
t.start()
currentThread().name='main one'
for j in range(4):
    # print('main',currentThread().getName()
    pass