import threading
import time


conA = threading.Condition()
conB = threading.Condition()
conC = threading.Condition()
def printA():
        while True:
            if conB.acquire() and conA.acquire():
                print 'A.'
                conB.notify()
                conB.release()
                conA.wait()

def printB():
        while True:
            if conB.acquire() and conC.acquire():
                print 'B.'
                conC.notify()
                conC.release()
                conB.wait()

def printC():
        while True:
            if conA.acquire() and conC.acquire():
                print 'C.'
                conA.notify()
                conA.release()
                conC.wait()

t1 = threading.Thread(target=printA)
t2 = threading.Thread(target=printB)
t3 = threading.Thread(target=printC)

t1.start()
t2.start()
t3.start()