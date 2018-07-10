import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    while True:
        # Do our die rolls
        roll1 = rand5()
        roll2 = rand5()
        print (roll1,roll2)
        outcome_number = (roll1-1) * 5 + (roll2-1) + 1
        print (outcome_number)

        # If we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            print ("hello2")
            continue

        # Our outcome was fine. return it!
        print ("hello1")
        return outcome_number % 7 + 1


print ('Rolling 7-sided die...')
print (rand7())