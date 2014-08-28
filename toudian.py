import random
a=0
b=100
data=[]
duchang=range(1000)
duchang=duchang[80::1]
flat=0
for nn in duchang:
    print str(nn)+" circle testing"
    for dc in range(100):
        data=[]
        for n in range(nn):
            x=random.random()*100
            y=random.random()*100
            data.append([x,y])
        cn=30000
        numyes=0
        print str(nn)+"circle      no."+str(dc)
        for n in range(cn):
        
            x=random.random()*100
            y=random.random()*100
            for n in data:
                if ((((x - n[0]) ** 2 + (y - n[1]) ** 2) ** 0.5)<=10):
                    numyes=numyes+1
                    break
        if ((float(numyes)/len(range(cn))*100)>=95):
            print "%"
            print float(numyes)/len(range(cn))*100
            print "numyes:"
            print numyes
            print "nn:"
            print nn
            flat=flat+1   
            break
    if (flat==1):
        break
