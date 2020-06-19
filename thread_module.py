from threading import Thread,current_thread

'''if we need current_thread we import the current thread '''

# def disp(a):
#     for i in range(5):
#          print('the child thread',a)
# t=Thread(target=disp,args=(10,))
# t.start()
# for i in range(5):
#     print('PVM')

'''we also give the argument in Thread function'''
'''set and get name in thread'''

# def dis():
#     print('child thread',current_thread().getName())
# t=Thread(target=dis)
# t.start()
# current_thread().setName('the main one')
# print('the new one',current_thread().getName())
# current_thread().name='main one'
# print('Main Thread',current_thread().getName())

'''video publish thread'''

def vid():
    current_thread().name='Video first'
    for i in range(5):
        print('Video publish 1',current_thread().getName())
vi=Thread(target=vid)
vi.start()
for i in range(5):
    print('video publish 2',current_thread().getName())