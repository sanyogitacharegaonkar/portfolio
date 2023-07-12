class sem1:
    def __init__(self,a1,b1,c1,d1,total1):
        self.a1=a1
        self.b1=b1
        self.c1=c1
        self.d1=d1
        self.total1 = self.a1 + b1 + c1 + d1
    def disp1(self):
        total1=self.a1+b1+c1+d1
        print("total1 of sem1:",self.a1+b1+c1+d1)
class sem2:
    def __init__(self,a2,b2,c2,d2,total2):
        self.a2=a2
        self.b2=b2
        self.c2=c2
        self.d2=d2
        self.total2 = self.a2 + b2 + c2 + d2
    def disp2(self):
        total2=self.a2+b2+c2+d2
        print("total2 of sem2:",self.a2+b2+c2+d2)
class student(sem1,sem2):
    def __init__(self,a1,b1,c1,d1,total1,a2,b2,c2,d2,total2,snm,dept,rn):
        sem1.__init__(self,a1,b1,c1,d1,total1)
        sem2.__init__(self,a2,b2,c2,d2,total2)
        self.snm=snm
        self.dept=dept
        self.rn=rn
    def calculate(self):
        calculate=total1+total2
        print("addition of sem1 and sem2:",self.total1+total2)
    def dip3(self):
        print("student name:",self.snm)
        print("department:", self.dept)
        print("rollno:", self.rn)
a1=float(input("enter a1 marks:"))
b1=float(input("enter b1 marks:"))
c1=float(input("enter c1 marks:"))
d1=float(input("enter d1 marks:"))
total1=float(input("enter total marks"))
a2=float(input("enter a2 marks:"))
b2=float(input("enter b2 marks:"))
c2=float(input("enter c2 marks:"))
d2=float(input("enter d2 marks:"))
total2=float(input("enter total marks"))
snm=input("student name:")
dept=input("department:")
rn=int(input("rollno:"))
s1=student(a1,b1,c1,d1,total1,a2,b2,c2,d2,total2,snm,dept,rn)
ca1=calculate()
s1.disp1()
s1.disp2()
s1.disp3()
ca1.calculate()



