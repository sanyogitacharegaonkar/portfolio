marks=int(input("enter a marks:"))
if(marks>=75and marks<=100):
    print(marks,"grade A+")
elif(marks>=65and marks<=75):
    print(marks,"grade A")
elif(marks>=55and marks<=65):
    print(marks, "grade B")
elif(marks>=45and marks<=55):
    print(marks, "grade c")
elif(marks>=35and marks<=45):
    print(marks,"pass")
else:
    print(marks,"fail")