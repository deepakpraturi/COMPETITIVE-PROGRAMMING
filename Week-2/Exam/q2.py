def unlock(li):
    k=[]
    for i in range(0,len(li)-1):
        for j in li[i]:
            print(j,len(li[i]),li[i],i)
            if(len(li[i])==1 and i==j):
                print("hello")
                pass

            else:
                k.append(j)
    print(k)

    for i in range(0,len(k)):
        if i in k:
            pass
        else:
            print("False")
            exit(0)
    print("True")


li=     [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]

unlock(li)