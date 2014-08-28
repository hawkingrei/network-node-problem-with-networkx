import random
a=500
b=600
data=[]
duchang=range(1000)
duchang=duchang[80::1]
flat=0
nn= 2000 #验证次数
while (True):
    if ((b-a)==1):
        c=b
        break
    c=int((a+b)/2)
    totalyes=0
    print str(c)+" circle testing"
    for dc in range(nn):
        data=[]
        for n in range(c):
            x=random.random()*100
            y=random.random()*100
            data.append([x,y])
        cn=10000 #验证投点数
        numyes=0
        print str(c)+"circle      no."+str(dc)
        for n in range(cn):
            x=random.random()*100
            y=random.random()*100
            for n in data:
                if ((((x - n[0]) ** 2 + (y - n[1]) ** 2) ** 0.5)<=10):
                    numyes=numyes+1
                    break;
        if (numyes==cn):
            totalyes=totalyes+1
    if (float(totalyes)/nn*100>=95):
        b=c
    else:
        if ((b-a)==1):
            c=b
            break
        a=c
    if (a==b):
        break
    if ((b-a)==1):
        break
    print float(totalyes)/nn*100
print "result:   "+str(c)
