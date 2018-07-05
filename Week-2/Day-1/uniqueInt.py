

def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    d={}
    count=0
    for i in delivery_ids:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    return d[i]




le=[2,2,2,2,3,3,3,1]
print(find_unique_delivery_id(le))












