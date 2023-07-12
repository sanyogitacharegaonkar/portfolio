sum=0
no=int(input("enter a no:"))
arg=no
while(no>0):
    r=no%10
    sum=sum+r*r*r
    no=no//10
if(arg==sum):
    print(arg,"is a armstrong")
else:
    print(arg,"is not armstrong")
