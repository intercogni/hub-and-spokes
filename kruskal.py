import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import numpy as np
import matplotlib.colors as mcolors

colors = [(0, 'lightblue'), (0.01, 'lightgreen'), (0.7, 'green'), (1, 'green')]  # Colors and positions
custom_cmap = mcolors.LinearSegmentedColormap.from_list("", colors)

def euclidean_distance(p1, p2):
   return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal_mst(graph):
   edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
   mst = nx.Graph()
   mst.add_nodes_from(graph.nodes())
   plt.gcf().set_facecolor('lightblue')
   # Graph(G, edge_layout='curved')
   
   x = np.random.rand(100)
   y = np.random.rand(100)
   
   components = {node: {node} for node in graph.nodes()}
   for edge in edges:
      u, v, weight = edge
      if components[u] != components[v]:
         mst.add_edge(u, v, weight=weight['weight'])
         components[u] |= components[v]
         for node in components[v]:
            components[node] = components[u]
            
         plt.clf()
         x = [graph.nodes[node]['pos'][0] for node in graph.nodes()]
         y = [graph.nodes[node]['pos'][1] for node in graph.nodes()]
         
         hb = plt.hexbin(x, y, gridsize=10, cmap=custom_cmap, extent=(0, 10000, 0, 10000))
            
         pos = nx.get_node_attributes(G, 'pos')
         nx.draw_networkx_nodes(G, pos, node_size=60, node_color='gray')
         # nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.05)
         nx.draw_networkx_edges(
            mst, 
            pos, 
            width=2.0, 
            alpha=0.75, 
            edge_color='black',
         )
         csfont = {'fontname':'Readex Pro'}
         plt.title("Kruskal's MST Algorithm Visualization", **csfont)
         plt.axis('off')
         plt.pause(0.33333)
   return mst

G = nx.Graph()

graph_data = []
edge_data = []
for i in range(ord('A'), ord('z') + 1):
   graph_data.append(
     (chr(i), {'pos': (random.randint(1, 10000), random.randint(1, 10000))})
   )
G.add_nodes_from(graph_data)

for i in range(ord('A'), ord('z') + 1):
   for j in range(ord('A'), ord('z') + 1):
      if i != j:
         edge_data.append((
            chr(i), 
            chr(j), 
            euclidean_distance(
               G.nodes[chr(i)]['pos'], 
               G.nodes[chr(j)]['pos']
            )
         ))
G.add_weighted_edges_from(edge_data)

# Calculate MST
fig = plt.figure()
mst = kruskal_mst(G)
plt.show()