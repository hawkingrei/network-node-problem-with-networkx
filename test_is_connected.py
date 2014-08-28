import networkx as nx
G=nx.Graph()
data=[]
data.append([0,0])
data.append([5,0])
data.append([2,0])
for n in range(3):
    G.add_node(n,pos=(data[n][0],data[n][1]))
for n in range(3):
    for m in range(n+1,3):
        distance=((data[m][0] - data[n][0]) ** 2 + (data[m][1] - data[n][1]) ** 2) ** 0.5
        if (distance<=10):
            G.add_edge(m+1,n+1,weigh=distance)
if 
