
rang=int(input("Enter the range."))+1
score=float(input("Your score?"))
ans=list(input("List your answers.").split(","))

def ngr(rang_,ans_,score_):
    for x in range(rang_):
        result=50
        for y in ans_:
            result-=round(abs(x-int(y))/4,0)
        if result==score_:
            print(x)

ngr(rang,ans,score)

input("Press enter to exit.")
