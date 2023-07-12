cibilscore=int(input("enter a cibilscore:"))
if(cibilscore>=750and cibilscore<=900):
    print(cibilscore,"Excellent")
elif(cibilscore>=650and cibilscore<=750):
    print(cibilscore,"Good")
elif(cibilscore>=550and cibilscore<=650):
    print(cibilscore, "Average")
elif(cibilscore>=300and cibilscore<=550):
    print(cibilscore, "Poor")
else:
    print(cibilscore,"Very Poor")
