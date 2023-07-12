sum=0
no=int(input("enter a no:"))
c=no
while(no>0):
    r=no%10
    sum=r+(sum*10)
    no=no/10
if(c==sum):
    print(c,"is a palindrome no")
else:
    print(c,"is not palindrome no")
