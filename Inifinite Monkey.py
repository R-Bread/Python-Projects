from random import choices, choice

def letter(i=0):
  if i==0:
      return choices([" "] + list("abcdefghijklmnopqrstuvwxyz"),
                     [18,6.5,1.23,2.73,2.64,10.24,1.97,1.53,4.141,6.21,0.1312,0.44,
                      3.34,2.058,5.92,6.26,1.75,0.098,5.15,5.34,7.61,2.24,0.86,1.377,
                      0.188,1.3612,0.0738])[0]
  elif i==1:
      return choice([" "] + list("abcdefghijklmnopqrstuvwxyz"))

def func(goal,i=0,k=0):
    result = ""
    for j in range(len(goal)):
      result+=letter(i)
    score = 0
    for x,y in zip(goal,result):
      if x==y: score+=1
    
    score = round(score * 100 / len(goal), 1)
    if k==0: print("\nGoal: '" + goal + "'", "Result: '" + result + "'", "Score: " + str(score) + "%", sep="\n")
    return score


x=True
#x=bool(input("Gameplay mode or stats?"))

while x:
    tries = 0
    max_score = 0
    score_ = 0
    goal_ = input("Goal: (No punctuation) ").lower()
    max_tries = int(input("Max tries:"))
    while tries <= max_tries:
        tries+=1
        score_ = int(func(goal_))
        if score_ > max_score: max_score = score_
        if score_ == 100:
            print("You win!")
            break
    else:
        print("That's all.\nYour maximum score was "+str(max_score)+"%.")
    y=input("Wanna go again? (y/n)")
    if y=="y":
        continue
    else:
        break


if not x:
    goals = [input().lower() for i in range(5)]
    max_tries=int(input("Max tries:"))
    for goal in goals:
        max_score0,max_score1=0,0
        score=0
        scores0,scores1 = [],[]
        for i in range(max_tries):
            score = int(func(goal,k=1))
            scores0.append(score) #Weighted
            if score>max_score0: max_score0=score
            score = int(func(goal,k=1,i=1))
            scores1.append(score)
            if score>max_score1: max_score1=score
        print(f"For '{goal}',\nWeighted: {sum(scores0)/len(scores0)} avg, {max_score0} max.\
        \nUn-weighted: {sum(scores1)/len(scores1)} avg, {max_score1} max.")


input("Press enter to exit.")