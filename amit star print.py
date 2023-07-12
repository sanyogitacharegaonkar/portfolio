str1=" "
for i in range(1,8):
    for j in range(1,24):
        if(i==1and j==1or i==1and j==2 or i==1and j==3 or i==1and j==4 or i==1and j==7 or i==1and
                j==13or i==1and j==15or i==1and j==16or i==1and j==17or i==1and
                j==19or i==1and j==20or i==1and j==20or i==1and j==21or i==1and
                j==22or i==1and j==23or i==2and j==1 or i==2and j==6or i==2and
                j==8 or i==2and j==9or i==2and j==13or i==2and j==14or i==2and
                j==17or i==2and j==22or i==3and j==1or i==3and j==6or i==3and
                j==8or i==3and j==10or i==3and j==12or i==3and j==14or i==3and
                j==17or i==3and j==22or i==4and j==1 or i==4and j==2or i==4and
                j==3 or i==4and j==4or i==4and j==5or i==4and j==6or i==4and
                j==8or i==4and j==11or i==4and j==14or i==4and j==17or i==4and
                j==22or i==5and j==1or i==5and j==6or i==5and j==8or i==5and
                j==14 or i==5and j==17or i==5and j==22or i==6and j==1or i==6and
                j==6or i==6and j==8or i==6and j==14 or i==6and j==17or i==6and
                j==22or i==7and j==1or i==7and j==6or i==7and j==8or i==7and
                j==14 or i==7and j==16or i==7and j==17or i==7and j==18or i==7and j==22):
            str1=str1+"*"
        else:
            str1=str1+" "
    str1=str1+"\n"
print(str1)