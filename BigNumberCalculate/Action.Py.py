from BigNumberAdd import *
from BigNumberMultiple import *


print "begin add process"
result=BigAdd([7,2,3,1,5],[1,2,3,4,5,6]);
print result;

print "begin multiplication process"
lista=[2,1,2,3,4,5,6,7,7]
listb=[2,1,3]
print MultipleLists(lista,listb)

print "begin divide process"

a=[4,2,3,1,5]
b=[2,3]
c=set(a)&set(b)
print c