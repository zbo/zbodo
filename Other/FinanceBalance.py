MonthRecords=[100.00
,489.12
,12454.12
,1234.10
,823.05
,109.20
,5.27
,1542.25
,839.18
,83.99
,1295.01
,1.75]
plusArray=[];
minusArray=[];
for i in range(1,len(MonthRecords)):
    monthCost=MonthRecords[i]-MonthRecords[i-1]
    if monthCost>0:
        plusArray.append(monthCost);
    else:
        minusArray.append(monthCost);
print plusArray;
print minusArray;

sum=0;
for p in plusArray:
    sum=sum+p;
print sum;
sum=0;
for m in minusArray:
    sum=sum+m;
print sum;