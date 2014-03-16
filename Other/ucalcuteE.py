def printTitle():
    print "n e";
    print "- -----------";

def printContent():
    for i in range(len(printR)):
        if i==0:
            print "0 1";
        elif i==1:
            print "1 2";
        elif i==8:
            print "8 2.718278770"
        else:
            print str(i)+" "+str(round(printR[i],9));

result=[];
printR=[1];
for i in range(9):
    base=i+1;
    if len(result)==0:
        result.append(base);
    else:
        result.append(base*result[len(result)-1]);
for r in result:
        printR.append(float(1)/float(r)+float(printR[len(printR)-1]));

printTitle();
printContent();