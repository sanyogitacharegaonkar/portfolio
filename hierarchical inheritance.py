class university:
    def __init__(self,unm,uloc,udcnt,uccnt,uscnt):
        self.unm=unm
        self.uloc=uloc
        self.udcnt=udcnt
        self.uccnt=uccnt
        self.uscnt=uscnt
    def disp1(self):
        print("university name:",self.unm)
        print("university location:",self.uloc)
        print("university department count:",self.udcnt)
        print("university college count:", self.uccnt)
        print("university student count:",self.uscnt)
class clg1(university):
    def __init__(self,unm,uloc,udcnt,uccnt,uscnt,clgnm,clgloc,cdcnt,cscnt):
        university.__init__(self,unm,uloc,udcnt,uccnt,uscnt)
        self.clgnm=clgnm
        self.clgloc=clgloc
        self.cdcnt=cdcnt
        self.cscnt=cscnt
    def disp2(self):
        print("college name:",self.clgnm)
        print("college location:", self.clgloc)
        print("college department count:", self.cdcnt)
        print("college student count:", self.cscnt)
class clg2(university):
    def __init__(self,unm,uloc,udcnt,uccnt,uscnt,clg2nm,clg2loc,c2dcnt,c2scnt):
        university.__init__(self,unm,uloc,udcnt,uccnt,uscnt)
        self.clg2nm=clg2nm
        self.clg2loc=clg2loc
        self.c2dcnt=c2dcnt
        self.c2scnt=c2scnt
    def disp3(self):
        print("college2 name:",self.clg2nm)
        print("college2 location:", self.clg2loc)
        print("college2 department count:", self.c2dcnt)
        print("college2 student count:", self.c2scnt)
unm=input("enter university name:")
uloc=input("enter university location:")
udcnt=int(input("enter university department count:"))
uccnt=int(input("enter university college count:"))
uscnt=int(input("enter university student count:"))
clgnm=input("enter college name:")
clgloc=input("enter college location:")
cdcnt=int(input("enter college department count:"))
cscnt=int(input("enter college student count:"))
clg2nm=input("enter college2 name:")
clg2loc=input("enter college2 location:")
c2dcnt=int(input("enter college2 department count:"))
c2scnt=int(input("enter college2 student count:"))
c1=clg1(unm,uloc,udcnt,uccnt,uscnt,clgnm,clgloc,cdcnt,cscnt)
c2=clg2(unm,uloc,udcnt,uccnt,uscnt,clg2nm,clg2loc,c2dcnt,c2scnt)
c1.disp1()
c1.disp2()
c2.disp3()