#NoBrains
import sys;
lines = int(sys.stdin.readline());
arrayList=[];
for i in range(lines):
	array = str(sys.stdin.readline());
	arrayList.append(array);
for array in arrayList:
	pair=array.split(' ');
	if int(pair[0])<int(pair[1]):
		print "NO BRAINS";
	else:
		print "MMM BRAINS";

