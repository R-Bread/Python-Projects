from random import randint,choices
#dificulty levels
dif=int(input("Choose a difficulty level.\n 0 for really easy,\n 1 for easy,\n 2 for medium,\n\
 3 for hard,\n and 4 for 2020.\n"))
diff=[(7,10,10,[2,1]),(5,15,20,[2,1]),(10,50,35,[1,1]),(5,100,45,[1,2]),(5,1089,60,[1,2])]
x,y,penalty,wlist=diff[dif]

ans=randint(0,y)

print(f"Guess the number!\nA number between 0 and {y} has been chosen. \
You have {x} chances, and the earlier you guess correctly, the more points you get!")
pnts=100

print(f"Your probability of winning is {round(100*(1-(1-1/(y+1))**x),2)}\%, so good luck!")

def pointreduce(o):
    return round(abs(ans-o)*125/x/y,0)

def hint(o):
    if ans<o:
        compare="less than"
    elif ans>o:
        compare="greater than"
    distant=f"about {abs(o-ans)+randint(-5,5)} away from"
    return "The answer's " + str(choices([compare,distant], weights=wlist)).strip("[']") + " your guess."

for i in range(x):
    guess=int(input("Guess a number."))
    if guess==ans:
        print(f"You win! You scored {pnts} points.")
        break
    else:
        print("Nope.", end=" ")
        if dif<4:
            print("Hint: ", hint(guess))
        pnts-=pointreduce(guess)
else:
    pnts-=penalty#might remove after complicating pointreduce().
    print("You lost. Too bad.",f"The corect answer was {ans}.",sep="\n")
    print(f"Still, you got {pnts} points!")

input("Press enter to exit.")
