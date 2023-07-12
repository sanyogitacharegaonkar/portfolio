class scl:
    def __init__(self,sclnm,sclloc,sdcnt,sscnt):
        self.sclnm=sclnm
        self.sclloc=sclloc
        self.sdcnt=sdcnt
        self.sscnt=sscnt
    def disp1(self):
        print("school name:",self.sclnm)
        print("school location:",self.sclloc)
        print("school department count:",self.sdcnt)
        print("school student count:",self.sscnt)
class clg:
    def __init__(self,clgnm,clgloc,cdcnt,cscnt):
         self.clgnm=clgnm
         self.clgloc=clgloc
         self.cdcnt=cdcnt
         self.cscnt=cscnt
    def disp2(self):
        print("college name:",self.clgnm)
        print("college location:", self.clgloc)
        print("college department count:", self.cdcnt)
        print("college student count:", self.cscnt)
class stud(scl,clg):
    def __init__(self,sclnm,sclloc,sdcnt,sscnt,clgnm,clgloc,cdcnt,cscnt,nm,rn,mark):
        scl.__init__(self,sclnm,sclloc,sdcnt,sscnt)
        clg.__init__(self,clgnm,clgloc,cdcnt,cscnt)
        self.nm=nm
        self.rn=rn
        self.mark=mark
    def disp3(self):
        print ("student name:",self.nm)
        print ("rollno:", self.rn)
        print ("mark:", self.mark)
sclnm=input("enter school name:")
sclloc=input("enter school location:")
sdcnt=int(input("enter school department count:"))
sscnt=int(input("enter school student count:"))
clgnm=input("enter college name:")
clgloc=input("enter college location:")
cdcnt=int(input("enter college department count:"))
cscnt=int(input("enter college student count:"))
nm=input("enter student name:")
rn=int(input("enter rollno:"))
mark=float(input("enter mark:"))
s1=stud(sclnm,sclloc,sdcnt,sscnt,clgnm,clgloc,cdcnt,cscnt,nm,rn,mark)
s1.disp1()
s1.disp2()
s1.disp3()