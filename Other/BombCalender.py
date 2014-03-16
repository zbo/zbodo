#zju 3403
import sys;

class BombDate:
    year=None;
    month=None;
    day=None;
    def __init__(self,year,month,day):
        self.year=year;
        self.month=month;
        self.day=day;
class BombMonth:
    year=None;
    month=None;
    def __init__(self,year,month):
        self.year=year;
        self.month=month;

def getMonthByYear(year):
    return year%12+1;

def getDayByYeaeAndMonth(year,month):
    if year%11==0 and month==1:
        return 2;
    else:
        return month**3;

def getBigger(BombMonth1,BombMonth2):
    if BombMonth1.year==BombMonth2.year:
        if BombMonth1.month>BombMonth2.month:
            return BombMonth1;
        else:
            return BombMonth2;
    else:
        if BombMonth1.year>BombMonth2.year:
            return BombMonth1;
        else:
            return BombMonth2;
def getMonthBetween(monthBigger,monthSmaller):
    monthList=[];
    if monthBigger.year==monthSmaller.year:
        for m in range(monthSmaller.month,monthBigger.month+1):
            monthList.append([monthBigger.year,m]);
    else:##monthBigger.year>monthSmaller.year
        for y in range(monthSmaller.year,monthBigger.year+1):
            start=1;
            end=getMonthByYear(y);
            if y==monthSmaller.year:
                start=monthSmaller.month;
            if y==monthBigger.year:
                end=monthBigger.month;
            for m in range(start,end+1):
                monthList.append([y,m]);
    return monthList;

def GetTotalDayFromMonthList(monthList):
    sumDay=0;
    for m in monthList:
        sumDay=sumDay+getDayByYeaeAndMonth(m[0],m[1]);
    return sumDay;

def getMonthBetweenAndCalDates(monthBigger,monthSmaller):
    #monthList=[];
    sumDay=0;
    if monthBigger.year==monthSmaller.year:
        for m in range(monthSmaller.month,monthBigger.month+1):
            #monthList.append([monthBigger.year,m]);
            sumDay=sumDay+getDayByYeaeAndMonth(monthBigger.year,m);
    else:##monthBigger.year>monthSmaller.year
        for y in range(monthSmaller.year,monthBigger.year+1):
            start=1;
            end=getMonthByYear(y);
            if y==monthSmaller.year:
                start=monthSmaller.month;
            if y==monthBigger.year:
                end=monthBigger.month;
            for m in range(start,end+1):
                #monthList.append([y,m]);
                sumDay=sumDay+getDayByYeaeAndMonth(y,m);
    return sumDay;


def calculateDays(date1,date2):
    list1=date1.split('-');
    list2=date2.split('-');
    BombDate1=BombDate(int(list1[2]),int(list1[0]),int(list1[1]));
    BombDate2=BombDate(int(list2[2]),int(list2[0]),int(list2[1]));
    if BombDate1.year==BombDate2.year and BombDate1.month==BombDate2.month:
        return abs(BombDate1.day-BombDate2.day);
    else:
        BombMonth1=BombMonth(int(list1[2]),int(list1[0]));
        BombMonth2=BombMonth(int(list2[2]),int(list2[0]));
        listtemp=[];
        listtemp.append(BombMonth1);
        listtemp.append(BombMonth2);
        monthBigger=getBigger(BombMonth1,BombMonth2);
        listtemp.remove(monthBigger);
        monthSmaller=listtemp[0];
        #monthList=getMonthBetween(monthBigger,monthSmaller);
        #print monthList
        #totalDays=GetTotalDayFromMonthList(monthList);
        totalDays=getMonthBetweenAndCalDates(monthBigger,monthSmaller);
        daybefore=BombDate1.day-1;
        dayafter=getDayByYeaeAndMonth(BombDate2.year,BombDate2.month)-BombDate2.day;
        return totalDays-daybefore-dayafter;

##date1='2-2-14';
##date2='2-3-15';
##monthBigger=BombMonth(1925,3);
##monthSmaller=BombMonth(1922,2);
##print calculateDays(date1,date2);
##print getMonthBetween(monthBigger,monthSmaller);
while 1:
    date1 = str(sys.stdin.readline());
    date2 = str(sys.stdin.readline());
    print calculateDays(date1,date2);