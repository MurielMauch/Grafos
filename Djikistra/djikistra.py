# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
from heapq import heappop, heappush
import sys
from matplotlib import pyplot as plt

def dijkstra (G, s): 
    push = heappush
    pop = heappop
    
    aux = G.copy()
    nodes = aux.nodes()
    
    for n in nodes:
        # iniciar todos os vertices com lambda = infinito e sem predecessor
        aux.node[n]['lambda'] = sys.float_info.max
        aux.node[n]['pi'] = None
    
    aux.node[s]['lambda'] = 0
    #iniciando dois vértices como 0
    aux.node[20]['lambda'] = 0
    #iniciando três vértices como 0
    aux.node[40]['lambda'] = 0

    # colocar o lambda do vertice inicial como 0
    
    Q = [] # fila de prioridades
    visited = []
    
    for n in nodes: 
        push(Q, (aux.node[n]['lambda'], n))
    
    while Q:
        u = pop(Q)       
        u = u[1]
        visited.append(u)
        for v in aux.neighbors(u):
            if v not in visited and aux.node[v]['lambda'] > (aux.node[u]['lambda'] + aux[u][v]['weight']):
                # tiro atual da fila 
                Q.remove((aux.node[v]['lambda'], v))
                aux.node[v]['lambda'] = aux.node[u]['lambda'] + aux[u][v]['weight'] # atualiza peso
                aux.node[v]['pi'] = u   # atualiza predecessor
                push(Q, (aux.node[v]['lambda'], v)) # atualiza valores na fila
    
    mst = nx.Graph()
    for v in aux.nodes():
        mst.add_node(v)
        if aux.node[v]['pi'] is not None: 
            u = aux.node[v]['pi']
            mst.add_edge(v, u)
            mst[v][u]['weight'] = aux[v][u]['weight']
    return mst 
    

def main ():
    A = np.loadtxt('wg59_dist.txt')
    G = nx.from_numpy_matrix(A)
    print G.nodes()
    D = dijkstra(G,0)
    pos = nx.spring_layout(D, k = 0.15, iterations=20)
    nx.draw_networkx(D, pos)
    dict_w = nx.get_edge_attributes(D,'weight')
    nx.draw_networkx_edge_labels(D, pos, labels = dict_w, font_size = 7, label_pos = 0.5)
    plt.show()

main()
