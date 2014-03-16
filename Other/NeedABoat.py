import sys;
import math;
from math import sqrt;

list=[];
years=[];
lines=int(sys.stdin.readline());
for i in range(lines):
	newline = str(sys.stdin.readline());
	list.append(newline);
for data in list:
	d=data.split(' ');
	r=sqrt(float(d[0])**2+float(d[1])**2);
	s=math.pi*r*r/2;
	years.append(int(s/50)+1);
index=1;
for year in years:
	print "Property "+str(index)+": This property will begin eroding in year "+str(year)+"." ;
	index=index+1;
print "END OF OUTPUT.";
