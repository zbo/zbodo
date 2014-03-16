'''
The GeoSurvComp geologic survey company is responsible for detecting underground 
oil deposits. GeoSurvComp works with one large rectangular region of land at a time,
and creates a grid that divides the land into numerous square plots. 
It then analyzes each plot separately, using sensing equipment to determine 
whether or not the plot contains oil. A plot containing oil is called a pocket. 
If two pockets are adjacent, then they are part of the same oil deposit. 
Oil deposits can be quite large and may contain numerous pockets. 
Your job is to determine how many different oil deposits are contained in a grid.

Input

The input file contains one or more grids. Each grid begins with a line 
containing m and n, the number of rows and columns in the grid, separated by 
a single space. If m = 0 it signals the end of the input; otherwise 1 <= m <= 100 
and 1 <= n <= 100. Following this are m lines of n characters each 
(not counting the end-of-line characters). Each character corresponds to one plot,
and is either `*', representing the absence of oil, or `@', representing an oil pocket.


Output

For each grid, output the number of distinct oil deposits. 
Two different pockets are part of the same oil deposit if they are adjacent 
horizontally, vertically, or diagonally. An oil deposit 
will not contain more than 100 pockets.


Sample Input

1 1
*
3 5
*@*@*
**@**
*@*@*
1 8
@@****@*
5 5 
****@
*@@*@
*@**@
@@@*@
@@**@
0 0


Sample Output

0
1
2
2
'''

array=[['*','*','*','*','@'],
       ['*','@','@','*','@'],
       ['*','@','*','*','@'],
       ['@','@','*','*','@'],
       ['@','@','*','*','*'],
       ]
currentMark=1

def checkCorner(row,col):
    if row>0 and col>0:#check upleft
        if array[row-1][col-1]=='@':
            array[row-1][col-1]=str(currentMark)
            markNeighbor(row-1,col-1)
    if row<len(array)-1 and col>0:#check downleft
        if array[row+1][col-1]=='@':
            array[row+1][col-1]=str(currentMark)
            markNeighbor(row+1,col-1)
    if col<len(array[0])-1 and row<len(array)-1:#check downright
        if array[row+1][col+1]=='@':
            array[row+1][col+1]=str(currentMark)
            markNeighbor(row+1,col+1)
    if col<len(array[0])-1 and row>0:#check upright
        if array[row-1][col+1]=='@':
            array[row-1][col+1]=str(currentMark)
            markNeighbor(row-1,col+1)

def checkUDLR(row,col):
    if row>0:#check up
        if array[row-1][col]=='@':
            array[row-1][col]=str(currentMark)
            markNeighbor(row-1,col)
    if row<len(array)-1:#check down
        if array[row+1][col]=='@':
            array[row+1][col]=str(currentMark)
            markNeighbor(row+1,col)
    if col>0:#check left
        if array[row][col-1]=='@':
            array[row][col-1]=str(currentMark)
            markNeighbor(row,col+1)
    if col<len(array[0])-1:#check right
        if array[row][col+1]=='@':
            array[row][col+1]=str(currentMark)
            markNeighbor(row,col+1)
        
        
def markNeighbor(row,col):
    checkUDLR(row,col)
    checkCorner(row,col)
    pass

print len(array[1])
for row in range(0,len(array)):
    for col in range(0,len(array[row])):
        if array[row][col]=='@':
            array[row][col]=str(currentMark)
            markNeighbor(row,col)
            currentMark=currentMark+1  
for item in array:
    print item
        