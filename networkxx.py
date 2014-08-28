import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random 
def get_edgelist(shortest_path):
     start =  "1"
     list_shortest_path = []
     for vertex in shortest_path:
          neighbor = (start,vertex)
          list_shortest_path.append(neighbor)
          start = vertex
     return list_shortest_path
G=nx.Graph()
data=np.loadtxt("data.txt").astype(int)
for n in range(120):
     G.add_node(str(data[n][0]),pos=(int(data[n][1]),int(data[n][2])))
pos=nx.get_node_attributes(G,'pos')
for m in range(120):
    for n in range(120):
        if (n<=m):
            continue
        distance=((data[m][1] - data[n][1]) ** 2 + (data[m][2] - data[n][2]) ** 2) ** 0.5
        if (distance<=10):
            G.add_edge(str(m+1),str(n+1),weigh=distance)
labels={}
for position in G.nodes():
     labels[position]=position
insertnodes=[]
for n in nx.dijkstra_path(G,"1","90"):
     for nn in G.neighbors(n):
          insertnodes.append(nn)
insertnodes=set(insertnodes)
nfigure=0
flat=0
for inodes in insertnodes:
     if (inodes==1 or inodes==90):
          break
     for n in nx.dijkstra_path(G,"1","90"):
          if n==inodes:
               flat=1
     if flat==1:
          flat=0
          continue
     print "³öÈëµã"+str(inodes)
     plt.figure(nfigure)
     result=(nx.dijkstra_path(G,"1",str(inodes)))+(nx.dijkstra_path(G,str(inodes),"90"))
     nx.draw_networkx_edges(G,pos,width=1,alpha=0.25,edge_color='gray')
     nx.draw_networkx_edges(G,pos,edge_labels={},edgelist=get_edgelist(result),width=8,alpha=0.5,edge_color='black')
     nx.draw_networkx_nodes(G,pos,nodelist=result,node_color='black',node_size=500,alpha=0.8)
     nx.draw_networkx_labels(G,pos,labels,font_size=9)
     print "result:"+str(result)
     nx.draw(G,pos,node_color='white')
     nfigure=nfigure+1
     if nfigure==10:
          break
plt.show()
