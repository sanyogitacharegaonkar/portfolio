str1=""
for i in range(1,6):
    for j in range(6,i-1):
        str1 =str1+" "
    for j in range(i,6):
        str1=str1+"*"
    str1=str1+"\n"
print(str1)