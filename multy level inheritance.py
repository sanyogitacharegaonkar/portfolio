class country:
    def __init__(self,cnm,carea,cpop,scnt):
         self.cnm=cnm
         self.carea=carea
         self.cpop=cpop
         self.scnt=scnt
    def disp1(self):
        print("country name:",self.cnm)
        print("country area:", self.carea)
        print("country population:", self.cpop)
        print("state count:", self.scnt)
class state(country):
    def __init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt):
        country.__init__(self,cnm,carea,cpop,scnt)
        self.snm=snm
        self.sarea=sarea
        self.spop=spop
        self.dcnt=dcnt
    def disp2(self):
        print("state name:",self.snm)
        print("state area:", self.sarea)
        print("state population:", self.spop)
        print("district count:",self.dcnt)
class district(state):
    def __init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt,dnm,darea,dpop,tcnt):
        state.__init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt)
        self.dnm=dnm
        self.darea=darea
        self.dpop=dpop
        self.tcnt=tcnt
    def disp3(self):
        print("district name:",self.dnm)
        print("district area:", self.darea)
        print("district population:", self.dpop)
        print("taluka count:", self.tcnt)
cnm=input("enter country name:")
carea=float(input("enter country area:"))
cpop=int(input("enter country population:"))
scnt=int(input("enter state count:"))
snm=input("enter state name:")
sarea=float(input("enter state area:"))
spop=int(input("enter state population:"))
dcnt=int(input("enter district count:"))
dnm=input("enter district name:")
darea=float(input("enter district area:"))
dpop=int(input("enter district population:"))
tcnt=int(input("enter taluka count:"))
d1=district(cnm,carea,cpop,scnt,snm,sarea,spop,dcnt,dnm,darea,dpop,tcnt)
d1.disp1()
d1.disp2()
d1.disp3()
