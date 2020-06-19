from threading import Thread

# class MyThread(Thread):
#     def run(self):
#             for i in range(5):
#                 print('the run')
# t=MyThread()
# t.start()
# t.join() # the join method is use for first execute the 
# for i in range(5):
#     print('main thread')


'''thread class with constructor'''

# class MyyThread(Thread):
#     def __init__(self,a):
#         for i in range(5):
#             Thread.__init__(self)
#             print('child class',a)

# tt=MyyThread(10)
# tt.start()
# for  i in range(5):
#     print('the main one') 

''' thread class without  use child class'''

class MyyyThread:
    def disp(self,a):
        print('child',a)

ttt=MyyyThread()
t=Thread(target=ttt.disp,args=(10,))
t.start()
print('the main one')