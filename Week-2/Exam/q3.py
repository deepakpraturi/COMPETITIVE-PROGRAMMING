def couple(li):
    c=0
    for i in range(0,len(li)-1):
        if i==li[i] or i+1 ==li[i]:
            pass
        else:
            c+=1
    print(c//2)

li=   [1,0]
couple(li)