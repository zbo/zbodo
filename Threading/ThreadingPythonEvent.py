import threading
import time


eventA = threading.Event()
eventB = threading.Event()
eventC = threading.Event()

def printA():
        while True:
            eventA.wait()
            print 'A.'
            eventA.clear()
            eventB.set()

def printB():
        while True:
            eventB.wait()
            print 'B.'
            eventB.clear()
            eventC.set()
            

def printC():
        while True:
            eventC.wait()
            print 'C.'
            eventC.clear()
            eventA.set()
            

t1 = threading.Thread(target=printA)
t2 = threading.Thread(target=printB)
t3 = threading.Thread(target=printC)

t1.start()
t2.start()
t3.start()
eventA.clear()
eventB.clear()
eventC.clear()
eventA.set()