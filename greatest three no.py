no1=int(input("enter a first no:"))
no2=int(input("enter a second no:"))
no3=int(input("enter a third no:"))
if(no1>no2):
    if(no1>no3):
        print(no1,"is greatest")
    elif(no2>no3):
        print(no2,"is greatest")
    else:
        print(no3,"is greatest")
else:
    print(no2,"is greatest")