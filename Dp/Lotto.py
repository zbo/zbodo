'''In a Lotto I have ever played, one has to select 6 numbers from the set {1,2,...,49}. 
A popular strategy to play Lotto - although it doesn't increase your chance of winning - is 
to select a subset S containing k (k>6) of these 49 numbers, and then play several games with choosing numbers only from S. 
For example, for k=8 and S = {1,2,3,5,8,13,21,34} there are 28 possible games: [1,2,3,5,8,13], 
[1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ... [3,5,8,13,21,34].

Your job is to write a program that reads in the number k and the set S and then prints all possible games choosing numbers only from S.
Input Specification
The input file will contain one or more test cases. Each test case consists of one line containing several integers separated from each other by spaces.
 The first integer on the line will be the number k (6 < k < 13). Then k integers, specifying the set S, will follow in ascending order. Input will be terminated by a value of zero (0) for k.
Output Specification
For each test case, print all possible games, each game on one line.
The numbers of each game have to be sorted in ascending order and separated from each other by exactly one space. 
The games themselves have to be sorted lexicographically, that means sorted by the lowest number first, 
then by the second lowest and so on, as demonstrated in the sample output below. 
The test cases have to be separated from each other by exactly one blank line. Do not put a blank line after the last test case.
Sample Input

7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

Sample Output

1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7
'''
"No memory table build for the recursive loop"
def pick(array,length):
    print array
    print length
    result=[]
    if(len(array)<length):
        result.append([])
        return result
    if(len(array)==length):
        result.append(array)
        return result
    else:
        temp=pick(array[1:],length)
        for item in temp:
            result.append(item)
        if length>0:
            temp=pick(array[1:],length-1)
            for item in temp:
                item.insert(0,array[0])
                result.append(item)
        return result
    

array=[1, 2, 3, 5, 8, 13, 21, 34]
for i in array:
    print i
print "lenght of the array is: "+str(len(array))
result=pick(array,6)
for item in result:
    print item
print len(result)
