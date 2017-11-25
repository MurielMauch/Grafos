# -*- coding: utf-8 -*-
from collections import deque 
import networkx as nx
from matplotlib import pyplot as plt

#PRECISA DE AJUSTES

def dfs(G,s):

    P = {}  

    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['pi'] = None

    global time 
    time += 1

    G.node[s]['ud'] = time
    G.node[s]['color'] = 'gray'

    Q = deque()
    Q.append(s)

    while (len(Q) > 0):
    #obtem o primeiro elemento da fila
        u = Q.popleft()
        G.node[s]['ud'] = time
        for v in G.neighbors(u):
            if (G.node[v]['color'] == 'white'):
                G.node[v]['pi'] = G.node[u]
                P[v] = u
                G.node[v]['color'] = 'gray'
                Q.append(v)
    
        G.node[u]['color'] = 'black'
        time+=1
        G.node[u]['uf'] = time

    return P

def main():
    G = nx.read_pajek('dolphins.paj')
    #print G.nodes()
    P = dfs(G,G.nodes()[0])
    #print 'P: ', P
    T = nx.Graph()
    #insere arestas em T
    T.add_edges_from([(u,v) for u, v in P.items()])
    #posicionamento do grafo T
    pos = nx.spring_layout(T)
    #plt.figure()
    #nx.draw(G, pos)
    #plt.show()
    #plt.close()
    #plt.figure()
    #print T.nodes()
    #plotar vertices de T
    nx.draw_networkx_nodes(T, pos, node_size=700)
    #obter dicionário com as distâncias
    #   QUERO MOSTRAR UF E UD 
    #   COMO???
    dist = { v: (v, data['uf']) for v, data in G.nodes(data=True)}
    #plotar arestas de T
    nx.draw_networkx_labels(T, pos, labels=dist)
    nx.draw_networkx_edges(T,pos)
    plt.show()
    #plt.close()

time = 0
main()