__author__ = 'zbo'
inputStr='''
Hallo, dies ist eine
ziemlich lange Zeile, die in Html
aber nicht umgebrochen wird.
<br>
Zwei <br> <br> produzieren zwei Newlines.
Es gibt auch noch das tag <hr> was einen Trenner darstellt.
Zwei <hr> <hr> produzieren zwei Horizontal Rulers.
Achtung       mehrere Leerzeichen irritieren

Html genauso wenig wie


mehrere Leerzeilen.
'''

#print inputStr

lines=[]
temp=''
allChars=inputStr.split();
for word in allChars:
    if word=='<br>':
        lines.append(temp)
        temp=''
    elif word=='<hr>':
        if temp!='':
            lines.append(temp)
        lines.append('--------------------------------------------------------------------------------')
        temp=''
    else:
        if len(temp+word)<80:
            if temp=='':
                temp=temp+word;
            else:
                temp=temp+" "+word;
        else:
            lines.append(temp)
            temp=word
if temp!='':
    lines.append(temp)
for line in lines:
    print line
