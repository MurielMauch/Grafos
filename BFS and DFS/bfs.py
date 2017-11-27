# -*- coding: utf-8 -*-
from collections import deque 
import networkx as nx 
import matplotlib.pyplot as plt

def bfs(G,s):

    #estrutura de dados que mapeia uma chave a um valor
    P = {}
    #inicializa todos os vértices como brancos
    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['lambda'] = float('inf')
    #inicializa a raiz como cinza e o custo da raiz é 0
    G.node[s]['color'] = 'gray'
    G.node[s]['lambda'] = 0
    #inicializa a fila Q como vazia e insere a raiz na fila
    Q = deque()
    Q.append(s) 
    #enquanto a fila não estiver vazia
    while (len(Q) > 0):
        #obtem o primeiro elemento da fila
        u = Q.popleft()
        for v in G.neighbors(u):
            if (G.node[v]['color'] == 'white'):
                G.node[v]['lambda'] = G.node[u]['lambda'] + 1
                P[v] = u
                G.node[v]['color'] = 'gray'
                Q.append(v)

        G.node[u]['color'] = 'black'

    return P

def main():
    G = nx.read_pajek('karate.paj')
    #print G.nodes()
    P = bfs(G,G.nodes()[10])
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
    dist = { v: (v, data['lambda']) for v, data in G.nodes(data=True)}
    #plotar arestas de T
    nx.draw_networkx_labels(T, pos, labels=dist)
    nx.draw_networkx_edges(T,pos)
    plt.show()
    #plt.close()

main()