import sys;
lines = int(sys.stdin.readline());
arrayList=[];
result=[];
while int(lines)!=-1:
	for i in range(lines):
		array = str(sys.stdin.readline());
		arrayList.append(array);
	currentSum=0;
	distanceSum=0;
	for array in arrayList:
		sepArray=array.split(' ');
		hours=int(sepArray[1])-currentSum;
		currentSum=int(sepArray[1]);
		distance=hours*int(sepArray[0]);
		distanceSum=distanceSum+distance;
	result.append(distanceSum);
	lines = int(sys.stdin.readline());
	arrayList=[];
for dis in result:
	print str(dis)+" miles";




