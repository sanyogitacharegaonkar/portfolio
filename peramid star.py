str1=""
for i in range(1,7):
    for k in range(1,7-i):
        str1=str1+" "
    for j in range(1,(i-1)+1):
        str1=str1+"* "
    str1=str1+"\n"
print(str1)