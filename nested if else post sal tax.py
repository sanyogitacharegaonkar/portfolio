

salary=int(input("enter the salary of employee:"))
if( salary>=50000):
    tax=(0.25*salary)
    print(salary,"CEO")
    print("tax",tax)
elif(salary>=40000):
    tax =(0.20*salary)
    print(salary," Manager")
    print("tax",tax)
elif(salary>=30000):
    tax =(0.15*salary)
    print(salary, "HR")
    print("tax",tax)
elif(salary>10000):
    tax =(0.10*salary)
    print(salary, "Senior employee")
    print("tax",tax)
elif(salary<=10000):
    print(salary,"fresher")
    print("no tax")
else:
    print("no employee")