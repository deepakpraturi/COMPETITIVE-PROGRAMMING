def search(list1,key):
    low=0
    high=len(list1)-1
    for i in range(len(list1)):
        # print("heelo")
        if(key<list1[low+high//2]):

            high=low+high//2
            print(high)
            if list1[high]==key:
                return True
        else:

            low=low+high//2
            print(low)
            if list1[low]==key:
                return True
    return False


li=[1,2,3,5,7,88,99]
k=1
print(search(li,k))


