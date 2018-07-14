def que(li):
    ki=sorted(li)
# print(ki)
    t=[]
    o=[]
    di={}
    di1={}
    temp=[[]]*len(li)
# print(temp,len(li))
    for i in li:
	    t.append(i[1])
	    o.append(i[0])
# print(t,o)
    k=sorted(t)
    p=sorted(o)
# print(k,p)
    for i in k:
	    if i in di:
		    di[i]+=1
	    else:
		    di[i]=1
    for i in p:
	    if i in di1:
		    di1[i]+=1
	    else:
		    di1[i]=1
# print(di,di1)
    for i in di:
	    if di[i]==1:
		    for j in range(0,len(li)):
			    if li[j][1]==i:
				    temp[i]=li[j]
			# print(i,temp)
    for i in temp:
	# print(i)
	    if i in ki:
		# print("hello")
		    ki.remove(i)
# print(ki)
    for i in range(0,len(ki)):
	    for j in range(i+1,len(ki)):
		    if ki[i][1]<=ki[j][1] and ki[i][0]<=ki[i][0]:
			    te=ki[i]
			    ki[i]=ki[j]
			    ki[j]=te
# print(ki)
    for i in range(len(temp)-1,-1,-1):
	    if temp[i]==[]:
		    temp[i]=ki.pop(0)

# for i in di1:
#     if i in temp[]:
#         di1[i]=0
# print(di1)
    print(temp)

que([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
que([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
que([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])