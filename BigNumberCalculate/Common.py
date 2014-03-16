__author__ = 'zbo'

def reverse(list):
    result=[];
    for i in range(len(list)-1,-1,-1):
        result.append(list[i])
    return result

def max(a,b):
    if a>=b:
        return a;
    else:
        return b;