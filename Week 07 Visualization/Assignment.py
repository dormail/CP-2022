import numpy.random
import networkx as nx
import matplotlib.pyplot as plt

def myErdos_Renyi(nodes, prob):
    G = nx.Graph()
    G.add_nodes_from(range(0, nodes))
    for i in range(0,nodes):
        for j in range(i+1, nodes):
            p = numpy.random.rand(1)
            if p < prob:
                G.add_edge(i,j)
    return G

# creating the graph
nodes = 100 # this should be 100 but it looks terrible
G = myErdos_Renyi(nodes,.1)

# plotting
nlarge = [(node) for (node, degree) in G.degree() if degree > 5]
nsmall = [(node) for (node, degree) in G.degree() if degree <= 5]


# nodes
pos = nx.spring_layout(G)  # positions for all nodes

nx.draw_networkx_nodes(G, pos,
                       nodelist = nlarge,
                       node_color='b',
                       node_size=700)
nx.draw_networkx_nodes(G, pos,
                       nodelist = nsmall,
                       node_color='r',
                       node_size=700)

# edges
nx.draw_networkx_edges(G, pos,
                       width=6)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()