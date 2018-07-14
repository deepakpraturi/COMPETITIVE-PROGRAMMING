li=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
li=[0, 1, 0, 2, 1, 0, 1]
li=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
li=[0, 1, 0, 2, 1, 0, 5, 1, 0, 2]
li=[0, 1, 0, 5, 1, 0, 2]
li=[0, 5, 1, 3, 4, 0, 1]
c=0
a=[0]*len(li)
b=[0]*len(li)
print(a,b)
a[0]=li[0]
b[len(li)-1]=li[len(li)-1]
for i in range(1,len(li)):
    a[i]=max(a[i-1],li[i])
for i in range(len(li)-2,0,-1):
    b[i]=max(b[i+1],li[i])
print(a,b)

for i in range(0,len(li)):
    #c+=max(a[i],b[i])-li[i]
    c+=min(a[i],b[i])-li[i]

print(c)