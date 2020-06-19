''' simple to use of class '''
# class Hotal:
#     def __init__(self,a):
#         self.a=a
    
#     def food(self):
#         for i in range(1,6):
#             print(self.a,i)

# h1=Hotal('Take the order')
# h2=Hotal('Recive the order')
# h1.food()
# h2.food()

from threading import Thread
class Hotal:
    def __init__(self,a):
        self.a=a
    
    def food(self):
        for i in range(1,6):
            print(self.a,i)

h1=Hotal('Take the order')
h2=Hotal('Recive the order')
t1=Thread(target=h1.food)

t2=Thread(target=h2.food)
t1.start()
t1.join()
t2.start()