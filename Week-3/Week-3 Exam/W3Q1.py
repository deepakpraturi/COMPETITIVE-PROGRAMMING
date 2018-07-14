x=1
y=4
a=str(bin(x))
b=str(bin(y))
print(a,b)
p=list(a)
q=list(b)
print(p,q)
c=0
while len(p)!=len(q):
    if len(p)>len(q):
        q.insert(2,0)
    else:
        p.insert(2,'0')
print(p,q)
for i in range(0,len(p)):
    if p[i]==q[i]:
        print(p[i],q[i])
        continue
    else:
        c+=1
print(c)