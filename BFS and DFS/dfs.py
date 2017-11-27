# -*- coding: utf-8 -*-
from collections import deque 
import networkx as nx
from matplotlib import pyplot as plt

#PRECISA DE AJUSTES

def dfs(G,s):

    #dicionario para armazenar antecessores
    P = {}
    #inicializa todos os nos como brancos 
    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['pi'] = None
    dfs_visit(G,s)

def dfs_visit(G,u):
    #dicionario
    global P 
    global time
    time += 1
    #tempo de entrada do nó
    G.node[u]['ud'] = time 
    G.node[u]['color'] = 'gray'
    for v in G.neighbors(u): 
        if (G.node[v]['color'] == 'white'):
            #atualiza o predecessor de v
            G.node[v]['pi'] = G.node[u]
            #coloco u como antecessor de v
            P[v] = u
            dfs_visit(G,v)
    G.node[u]['color'] = 'black'
    time += 1
    G.node[u]['uf'] = time 

def main():
    global P
    G = nx.read_pajek('dolphins.paj')
    #print G.nodes()
    dfs(G,G.nodes()[25])
    #print G.nodes()[25]
    T = nx.Graph()
    #insere arestas em T
    T.add_edges_from([(u,v) for u, v in P.items()])
    #posicionamento do grafo T
    pos = nx.spring_layout(T)
    nx.draw_networkx_nodes(T, pos, node_size=700)
    #obter dicionário com as distâncias
    ud = {v: (v, data['ud']) for v, data in G.nodes(data=True)}
    #uf = {v: (v, data['uf']) for v, data in G.nodes(data=True)}
    nx.draw_networkx_labels(T, pos, labels=ud, font_size = 8, label_pos = 0.5)
    nx.draw_networkx_edges(T,pos)
    plt.show()

time = 0
P = {}
main()