import threading
import etoken

myLock=threading.Lock()
message="this is a message"

def operateToken():
    myLock.acquire()
    token.login("safenet123$")
    print token.pkcs7_seal(message)
    myLock.release()
    
token = etoken.eToken(engpath="I:\zboDo\etoken\engines")
t1 = threading.Thread(target=operateToken)
t2 = threading.Thread(target=operateToken)
t3 = threading.Thread(target=operateToken)

t1.start()
t2.start()
t3.start()