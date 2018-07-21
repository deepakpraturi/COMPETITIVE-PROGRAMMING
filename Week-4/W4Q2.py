x=15
c=0
ca=[]
for i in range(0,x+1):
    print(i)
    c=0
    a=bin(i)
    li=list(a)
    print(li)
    for i in li:
        print(i)
        if i=='1':
            print("hello")
            c+=1
            print("c:",c)
    ca.append(c)

print(ca)