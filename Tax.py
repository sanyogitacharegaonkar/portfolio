salary=int(input("enter a salary:"))
if(salary<=10000):
    print("no tax")
elif(salary>=10000and salary<=20000):
    tax=(0.10*salary)
    print("tax=",tax)
elif(salary>=20000and salary<=30000):
    tax=(0.20*salary)
    print("tax=",tax)
else:
    tax=(0.25*salary)
    print("tax=",tax)