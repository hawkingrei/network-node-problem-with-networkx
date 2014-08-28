import random
import networkx as nx
a=0
b=100
data=[]
duchang=range(1000)
duchang=duchang[1::1]
flat=0
for nn in duchang:
    print str(nn)+" circle testing"
    for dc in range(40):
        data=[]
        G=nx.Graph()
        is_connect=0
        while(is_connect==0):
            for n in range(nn):
                x=random.random()*100
                y=random.random()*100
                data.append([x,y])
                G.add_node(n,pos=(x,y))
            for n in range(nn):
                for m in range(n+1,nn):
                    distance=((data[m][0] - data[n][0]) ** 2 + (data[m][1] - data[n][1]) ** 2) ** 0.5
                    if (distance<=10):
                        G.add_edge(m,n,weigh=distance)
            if (len(G.edges())+1==len(G.nodes())):
                is_connect=1
            else:
                G.clear()
        cn=1500
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
