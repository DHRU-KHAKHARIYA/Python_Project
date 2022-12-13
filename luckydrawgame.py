import random
print(100*"*")
print("|                                         LUCKY DRAW GAME                                          |")
print(100*"*")
print("")
print(100*"=")
lb=int(input("ENTER LOWER B0UND:"))
ub=int(input("ENTER UPPER BOUND:"))
rnnum = random.randint(lb,ub)
attempt=0
i=1
print("                           <<< GUESS IN FIRST CHANCE TO WIN 30 POINTS >>>                           ")
print("                          <<<  GUESS IN SECOND CHANCE TO WIN 20 POINTS  >>>                          ")
print("                           <<< GUESS IN THIRD CHANCE TO WIN 10 POINTS >>>                           ")
print("-------------------------------------------TRY YOUR LUCK--------------------------------------------")
while i<=3:
    if i==1:
        guess=int(input("FIRST CHANCE:"))
    elif i == 2:
        guess = int(input("SECOND CHANCE:"))
    else :
        guess = int(input("LAST CHANCE:"))
    if guess==rnnum and i==1:
        print("SCORE = 30 POINTS!!!")
        print("------------------------------------------CONGRATULATIONS-------------------------------------------")
        break
    elif guess==rnnum and i==2:
        print("SCORE = 20 POINTS!!!")
        print("------------------------------------------CONGRATULATIONS-------------------------------------------")
        break
    elif guess == rnnum and i == 3:
        print("SCORE = 10 POINTS!!!")
        print("------------------------------------------CONGRATULATIONS-------------------------------------------")
        break
    else:
        if rnnum > guess:
            attempt += 1
            if attempt==3:
                print("---------------------------------------BETTER LUCK NEXT TIME----------------------------------------")

            else:
                print("TOO LOW")
                print("HAVE ONE MORE TRY")

        else:
            attempt += 1
            if attempt == 3:
                print("---------------------------------------BETTER LUCK NEXT TIME----------------------------------------")

            else:
                print("TOO HIGH")
                print("HAVE ONE MORE TRY")

    i=i+1
print(100*"=")
