def change_possibilities(amount, denominations):
    r = [0] * (amount + 1)

    r.insert(0, 1)
    len(r)
    for i in denominations:
        for j in range(i, len(r) - 1):
            if (j >= i):
                r[j] = (r[j] + r[j - i])
    return r[amount]

amount=5
denom=[1,2,3]
print(change_possibilities(amount,denom))