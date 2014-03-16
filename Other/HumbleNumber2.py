import time
t1=time.time();
pindex=[0,0,0,0];
prim=[2,3,5,7];
result=[1];

for i in range(5842):
    for j in range(4):
        while result[pindex[j]]*prim[j]<=result[i]:
            pindex[j]=pindex[j]+1;
    min=2000000001;
    for j in range(4):
        if result[pindex[j]]*prim[j]<min:
            min=result[pindex[j]]*prim[j];
    result.append(min);

print result[99];
t2=time.time();
print t2-t1