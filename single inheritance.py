class clg:
    def __init__(self,clgnm,clgloc,dcnt,scnt):
         self.clgnm=clgnm
         self.clgloc=clgloc
         self.dcnt=dcnt
         self.scnt=scnt
    def disp1(self):
        print("college name:",self.clgnm)
        print("college location:", self.clgloc)
        print("department count:", self.dcnt)
        print("student count:", self.scnt)
class stud(clg):
    def __init__(self,clgnm,clgloc,dcnt,scnt,nm,rn,mark):
        clg.__init__(self,clgnm,clgloc,dcnt,scnt)
        self.nm=nm
        self.rn=rn
        self.mark=mark
    def disp2(self):
        print ("student name:",self.nm)
        print ("rollno:", self.rn)
        print ("mark:", self.mark)
clgnm=input("enter college name:")
clgloc=input("enter college location:")
dcnt=int(input("enter department count:"))
scnt=int(input("enter student count:"))
nm=input("enter student name:")
rn=int(input("enter rollno:"))
mark=float(input("enter mark:"))
s1=stud(clgnm,clgloc,dcnt,scnt,nm,rn,mark)
s1.disp1()
s1.disp2()





