# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
from heapq import heappop, heappush
import sys
from matplotlib import pyplot as plt

def prim (G, s): 
    #inicializa a pilha
    push = heappush
    pop = heappop
    #copia o grafo em uma variável auxiliar
    aux = G.copy()
    nodes = aux.nodes()
    
    for n in nodes:
        # iniciar todos os vertices com lambda = infinito e sem predecessor
        aux.node[n]['lambda'] = float('inf')
        aux.node[n]['pi'] = None

    # colocar o lambda do vertice inicial como 0
    aux.node[s]['lambda'] = 0
   
    Q = [] # fila de prioridades
    visited = [] #fila para os vértices visitados
    
    for n in nodes: 
        #coloca o vértice na fila
        push(Q, (aux.node[n]['lambda'], n))
    
    while Q:
        #tira o vértice da lista e o coloca na fila de visitados
        u = pop(Q)       
        u = u[1]
        visited.append(u)
        #para cada vizinho do vértice u, se ele não foi visitado e seu custo é menor
        for v in aux.neighbors(u):
            if v not in visited and aux.node[v]['lambda'] > aux[u][v]['weight']:
                # tiro atual da fila 
                Q.remove((aux.node[v]['lambda'], v))
                aux.node[v]['lambda'] = aux[u][v]['weight'] # atualiza peso
                aux.node[v]['pi'] = u   # atualiza predecessor
                push(Q, (aux.node[v]['lambda'], v)) # atualiza valores na fila
    #inicializa o grafo
    mst = nx.Graph()
    #adiciona os nós e seus valores ao grafo, que será retornado
    for v in aux.nodes():
        mst.add_node(v)
        if aux.node[v]['pi'] is not None: 
            u = aux.node[v]['pi']
            mst.add_edge(v, u)
            mst[v][u]['weight'] = aux[v][u]['weight']
    return mst 

def main ():
    #lê e transforma uma matrix de adjacência em um grafo
    A = np.loadtxt('ha30_dist.txt')
    G = nx.from_numpy_matrix(A)
    #H recebe a chamada do algoritmo prim
    H = prim(G,G.nodes()[0])
    #desenha o grafo
    pos = nx.spring_layout(H, k = 0.15, iterations=20)
    nx.draw_networkx(H, pos)
    dict_w = nx.get_edge_attributes(H,'weight')
    nx.draw_networkx_edge_labels(H, pos, labels = dict_w, font_size = 7, label_pos = 0.5)
    plt.show()

main()
