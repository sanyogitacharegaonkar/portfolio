salary=int(input("enter a salary:"))
if(salary>=4000000and salary<=5000000):
    print(salary,"CEO")
elif(salary>=3000000and salary<=4000000):
    print(salary,"Senior Manager")
elif(salary>=1500000and salary<=3000000):
    print(salary, "Manager")
elif(salary>=1000000and salary<=1500000):
    print(salary, "Team Leader")
elif(salary>=500000and salary<=1000000):
    print(salary,"Senior Employee")
else:
    print(salary,"fresher")