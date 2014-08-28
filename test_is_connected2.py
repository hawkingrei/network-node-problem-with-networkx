import random
import networkx as nx
a=0
G=nx.Graph()
b=100
data=[]
nn=2
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
print "ok"
