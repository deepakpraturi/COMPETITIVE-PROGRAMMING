x=12354
y=bin(x)
print(y)
li=list(y)
print(li)
co=1
c=[]
for i in range(0,len(li)):
    #print(i)
    if li[i]=='1':
        for j in range(i+1,len(li)):

            #print(j)
            if li[j]=='1':
                #print("hello")
                c.append(co)
                co=0
            else:
                co += 1

print(max(c))