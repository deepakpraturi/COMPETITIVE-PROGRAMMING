def anagram(t,s):
    t=t.lower()
    s=s.lower()
    t1=list(t)
    t2=list(t)
    s1=list(s)
    for i in t2:
        if i ==' ':
            t2.remove(i)
    #print(t1,s1)
    for i in t1:
        #print(i)
        if i in s1:
            t2.remove(i)
    #print(t2)
    if len(t2)==0:
        return True
    else:
        return False
t="Dirty Room"
s="Dormitory"
print(anagram(t,s))