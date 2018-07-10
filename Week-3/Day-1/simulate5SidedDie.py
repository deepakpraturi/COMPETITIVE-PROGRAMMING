import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    x=rand7()
    if x==1 or x==2:
        #print "hello"
        return x
    else:
        return x-2




print ('Rolling 5-sided die...')
print (rand5())