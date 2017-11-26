# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
from heapq import heappop, heappush
import sys
from matplotlib import pyplot as plt

def prim (G, s): 
    push = heappush
    pop = heappop
    
    aux = G.copy()
    nodes = aux.nodes()
    
    for n in nodes:
        # iniciar todos os vertices com lambda = infinito e sem predecessor
        aux.node[n]['lambda'] = float('inf')
        aux.node[n]['pi'] = None

    # colocar o lambda do vertice inicial como 0
    aux.node[s]['lambda'] = 0
   
    Q = [] # fila de prioridades
    visited = []
    
    for n in nodes: 
        push(Q, (aux.node[n]['lambda'], n))
    
    while Q:
        u = pop(Q)       
        u = u[1]
        visited.append(u)
        for v in aux.neighbors(u):
            if v not in visited and aux.node[v]['lambda'] > aux[u][v]['weight']:
                # tiro atual da fila 
                Q.remove((aux.node[v]['lambda'], v))
                aux.node[v]['lambda'] = aux[u][v]['weight'] # atualiza peso
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
'''    
def calcular_peso(T): 
    peso = 0
    pesos = nx.get_edge_attributes(T, 'weight')
    for v in T.edges(): 
        peso += pesos[v]
    return peso      
'''
def main ():
    A = np.loadtxt('ha30_dist.txt')
    G = nx.from_numpy_matrix(A)
    #print G.nodes()
    H = prim(G,0)
    #peso = calcular_peso(H)
    #print("Peso:",peso)
    #print(nx.is_forest(H))
    pos = nx.spring_layout(H, k = 0.15, iterations=20)
    nx.draw_networkx(H, pos)
    dict_w = nx.get_edge_attributes(H,'weight')
    #print (dict_w)
    nx.draw_networkx_edge_labels(H, pos, labels = dict_w, font_size = 8, label_pos = 0.5)
    #plt.savefig('dijkstra_test3.pdf')
    plt.show()

main()
