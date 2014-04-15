#this is comments
def printArray(array):
    for i in range(len(array)):
        print array[i];

def BuildUpLeftBrace(number):
    for i in range(number):
        structure.append('(');

def BuildUpRightBrace():
    structure.append(')');


def GetAdditionLeftBrace(i):
    if i==0:
        return p_array[i];
    else:
        return p_array[i]-p_array[i-1];

def ConstructSequence(p_array):
    for i in range(len(p_array)):
        AdditionalLeft=GetAdditionLeftBrace(i);
        BuildUpLeftBrace(AdditionalLeft);
        BuildUpRightBrace();

def ConstructWSequence(structure):
    for i in range(len(structure)):
        if structure[i]==')':
            w_array.append(GetEnClosedLeftBrace(i));

def GetEnClosedLeftBrace(i):
    NumberOfLeftBrace=0;
    NumberOfRightBrace=1;
    while NumberOfRightBrace>0:
        i=i-1;
        if structure[i]=='(':
            NumberOfRightBrace=NumberOfRightBrace-1;
            NumberOfLeftBrace=NumberOfLeftBrace+1;
        else:
            NumberOfRightBrace=NumberOfRightBrace+1;
    return NumberOfLeftBrace;


p_sequence="466668999"
structure=[];
p_array=[];
w_array=[];
for i in range(len(p_sequence)):
    p_array.append(int(p_sequence[i]));

ConstructSequence(p_array);
ConstructWSequence(structure);
printArray(structure);
print("---------------")
printArray(w_array);






