class fishnet:
    Info=[]
    Edge=[]
class angle:
    node=None
    branch=[]

def PrintFishNet(fishnet):
    print fishnet.Info
    print fishnet.Edge
def PrintAngles(angle):
    print "node is : "+str(angle.node)
    print "brach are : "
    print angle.branch
    
def DeleteAngles(AngleList):
    for angle in AngleList:
        net.Info[0][0]=net.Info[0][0]-1#delete one angle node
        net.Info[0][1]=net.Info[0][1]-2#delete two branches
        for index in range(len(net.Edge)-1,-1,-1):
            if angle.branch[0]==net.Edge[index] or angle.branch[1]==net.Edge[index]:
                net.Edge.remove(net.Edge[index]) 

def FindRelatedEdges(i,Edge):
    relate=[]
    for edge in Edge:
        if edge[0]==i or edge[1]==i:
            relate.append(edge)
    return relate

def JudgeAngleClosed(relatedEdges,i,Edge):
    edge0=set(relatedEdges[0])
    edge1=set(relatedEdges[1])
    tempMerge=edge0|edge1
    tempMerge.discard(i)
    templist=list(tempMerge)
    
    if list(Edge).__contains__(templist):
        return 1
    templist.reverse()
    if list(Edge).__contains__(templist):
        return 1
    return 0;

def FindAngleNode(Edge,NodeCount):
    AngleList=[]
    for i in range(1,NodeCount+1):
        relatedEdges=FindRelatedEdges(i,Edge)
        if len(relatedEdges)==2:
            if JudgeAngleClosed(relatedEdges,i,Edge)==1:
                Angle=angle()
                Angle.node=i
                Angle.branch=relatedEdges
                AngleList.append(Angle)
    return AngleList

def JudegFishNet():
#    PrintFishNet(net)
    NodeCount=net.Info[0][0]
    EdgeCount=net.Info[0][1]
    Edge=net.Edge
    AngleList=FindAngleNode(Edge,NodeCount)
    if len(AngleList)>0:
        DeleteAngles(AngleList)
        JudegFishNet()
    else:
        if NodeCount>2:
            print 'Imperfect'
        else:
            print 'Perfect'
    
netEdge=[];
netInfo=[];
netInfo.append([6,8])
netEdge.append([1,2])
netEdge.append([2,3])
netEdge.append([3,4])
netEdge.append([4,5])
netEdge.append([5,6])
netEdge.append([6,1])
netEdge.append([1,3])
netEdge.append([4,6])
#netEdge.append([4,1])

net=fishnet()
net.Info=netInfo
net.Edge=netEdge
JudegFishNet()


    
    