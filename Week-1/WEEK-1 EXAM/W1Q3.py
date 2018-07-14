def se(g):
    t=[]
    x=0
    y=0
    a=0
    ta=[]
    for i in range(0,len(g)):
    # print(i)
    # print(g[i],len(g[i]))
        for j in range(0,len(g[i])):
            if g[i][j]==1:
                t.append([i,j])
# print(t)
    for i in t:
        x+=i[0]
        y+=i[1]
# print(x//len(t),y//len(t))
    if x!=0 and y!=0:
        ta=[x//len(t),y//len(t)]
    else :
        ta=[0,0]
# target=len(g[i])//2
# print(target)
# ta=[0,target]
# print(ta)
# print(t)
    l=[]
# print("ta :",ta)
    for i in t:
        k=abs(ta[0]-i[0])
        j=abs(ta[1]-i[1])
        a=k+j+a
    print(a)

se([[1,0,1,0,1],[0,0,0,0,0],[0,0,1,0,0]])
se([[1,0,1,0,1],[0,1,0,0,0],[0,1,1,0,0]])
se([[1,1],[1,1]])
se([[1,0],[0,0]])
se([[0,0],[0,0]])

# g=[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# g=[[1,1],[1,1]]
# g=[[1,0],[0,0]]
# g=[[0,0],[0,0]]