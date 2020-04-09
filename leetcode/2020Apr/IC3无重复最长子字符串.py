def lengthOfLongestSubstring(s):
    temp = []
    max = 0
    for c in s:
        if len(temp)==0:
            temp.append(c)
        else:
            if not c in temp:
                temp.append(c)
            else:
                if len(temp)>max:
                    max = len(temp)
                index = temp.index(c)
                temp = temp[index+1:]
                print(temp)
                temp.append(c)
    if len(temp)>max:
        max = len(temp)
    return max

if __name__ == "__main__":
    print(lengthOfLongestSubstring("dvdf"))