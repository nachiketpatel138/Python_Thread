from threading import Thread
from time import sleep
class MyExam:
    def Myquestion(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print('first')
        sleep(2)
    def q2(self):
        print('second')
        sleep(2)
    def q3(self):
        print('third')
        sleep(2)

mte=MyExam()
t=Thread(target=mte.Myquestion)
t.start()