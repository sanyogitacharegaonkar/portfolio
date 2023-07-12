str1=""
for i in range(1,7):
    for j in range(1,9):
        if(i==1 and j==3  or i==1 and j==5 or i==1 and j==6 or i==1 and j==7 or i==1 and j==8 or i==2 and j==2
                or i==2 and j==4 or i==2 and j==8 or i==3 and j==1 or i==3 and j==2 or i==3 and j==3 or i==3 and
                j==4 or i==3 and j==5 or i==3 and j==6 or i==3 and j==7 or i==3 and j==8 or i==4 and j==1 or i==4
                and j==4 or i==4 and j==8 or i==5 and j==1 or i==5 and j==4 or i==5 and j==8 or i==6):
            str1=str1+"*"
        else:
            str1=str1+" "
    str1=str1+"\n"
print(str1)