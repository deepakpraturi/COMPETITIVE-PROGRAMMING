def find_duplicate(list):
    n = len(list)
    i = n
    j = n
    while True:
        i = list[i - 1]
        j = list[j - 1]
        j = list[j - 1]
        if i == j:
            break

    j = n
    while True:
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
            break

    return i

li=[8,3,5,2,4,5,6,7,1]
print(find_duplicate(li))