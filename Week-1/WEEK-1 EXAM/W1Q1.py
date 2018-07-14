li={
'A' :".-",
'B':"-...",
'C' :"-.-.",
'D' :"-..",
'E' :".",
'F' :"..-.",
'G' :"--.",
'H' :"....",
'I' :"..",
'J' :".---",
'K' :"-.-",
'L' :".-..",
'M' :"--",
'N' :"-.",
'O' :"---",
'P' :".--.",
'Q' :"--.-",
'R' :".-.",
'S' :"...",
'T' :"-",
'U' :"..-",
'V' :"...-",
'W' :".--",
'X' :"-..-",
'Y' :"-.--",
'Z' :"--.."	}
test=[]
test.append(["gin","zen","gig","msg"])
test.append(["a", "z", "g", "m"])
test.append( ["bhi", "vsv", "sgh", "vbi"])
test.append( ["a", "b", "c", "d"])
test.append( ["hig", "sip", "pot"])
tl=[]
for wl in test:
    di={}
    s=""
    tl=[]
    # print(di)
    for word in wl:
        WORD=word.upper()
        s=""
        w=list(WORD)
        # print(w)
    # print(w)
        t=[]
        for i in w:
            t.append(li[i])
    # print(t)
        for j in t:
            s+=j
    # print(s)
        tl.append(s)
        # print(tl)
# print(tl)
    di={}
    for i in tl:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    print(len(di))
