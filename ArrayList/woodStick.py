def PrintWoodArray(woodArray):
    for i in range(len(woodArray)):
        print "weight:"+str(woodArray[i].weight)+" length:"+str(woodArray[i].length);

def FindMinWeight(woodArray):
    if len(woodArray)==0:
        return None;
    else:
        w=woodArray[0];
        for i in range(len(woodArray)):
            if woodArray[i].weight<w.weight:
                w=woodArray[i];
        return w;

def FindNextWood(woodArray,arrangedLastWood):
    if woodArray.count==0:
        return None;
    else:
        w=None;
        for i in range(len(woodArray)):
            if woodArray[i].weight>arrangedLastWood.weight and woodArray[i].length>arrangedLastWood.length:
                if w==None:
                    w=woodArray[i];
                elif woodArray[i].weight<=w.weight and woodArray[i].length<=w.length:
                    w=woodArray[i];
    return w;
                    
class wood:pass; 
array=[4,9,5,2,2,1,3,5,1,4]
woodArray=[];
ArrangedArray=[];
for i in range(0,len(array),2):
    w=wood();
    w.weight=array[i];
    w.length=array[i+1];
    woodArray.append(w);

minWeightWood=FindMinWeight(woodArray);
while minWeightWood!=None:
    ArrangedArray.append(minWeightWood);
    woodArray.remove(minWeightWood);
    nextWood=FindNextWood(woodArray,ArrangedArray[len(ArrangedArray)-1]);
    while nextWood!=None:
        ArrangedArray.append(nextWood);
        woodArray.remove(nextWood);
        nextWood=FindNextWood(woodArray,ArrangedArray[len(ArrangedArray)-1]);
    minWeightWood=FindMinWeight(woodArray);
PrintWoodArray(ArrangedArray);
PrintWoodArray(woodArray);
