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
    #incrementa o tempo
    global time 
    time += 1
    #inicia a raiz com a cor cinza e define seu tempo de entrada
    #G.node[u]['ud'] = time
    G.node[u]['color'] = 'gray'
    #inicia a fila Q fazia e insere a raiz na fila
    Q = deque()
    Q.append(s)
    #inicia a fila auxiliar
    visited = []
    #enquanto fila não estiver vazia
    while (len(Q) > 0):
    #obtem o primeiro elemento da fila
        u = Q.popleft()
        #define o tempo de entrada
        G.node[u]['ud'] = time
        #insere u na fila de visitados
        visited.append[u]
        for v in G.neighbors(u):
            #coloco todos os vizinhos na fila
            Q.append(v)

        #tira w da fila de visitados
        w = Q.popleft()
        if (G.node[w]['color'] == 'white' and w not in visited):
            #atualiza o predecessor de v
            G.node[w]['pi'] = G.node[u]
            #coloco u como antecessor de v
            P[w] = u
            #indico que v foi visitado
            G.node[w]['color'] = 'gray'
            visited.append[w]

    G.node[u]['color'] = 'black'
    time+=1
    G.node[u]['uf'] = time

    return P

def main():
    G = nx.read_pajek('dolphins.paj')
    #print G.nodes()
    P = dfs(G,G.nodes()[25])
    #print G.nodes()[25]
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
    #TESTE 1 
    '''
    nx.draw_networkx(T, pos)
    dict_w = nx.get_edge_attributes(T,'uf')
    nx.draw_networkx_edge_labels(T, pos, labels = dict_w, font_size = 7, label_pos = 0.5)
    plt.show()
    '''
    #FIM TESTE 1
    #TESTE 2
    #dist = { v: (v, data['ud'], data1['ufs']) for v, data, data1 in G.nodes(data=True)}
    dist = { v: (v, data['ud']) for v, data in G.nodes(data=True)}
    print 'TESMPO DE ENTRADA'
    print dist
    dist = { v: (v, data['uf']) for v, data in G.nodes(data=True)}
    print 'TESMPO DE SAIDA'
    print dist
    '''
    for i in dist:
        dist[i] = []
        dist[i].append({ v: (v, data['ud']) for v, data in G.nodes(data=True)})
    print dist.items()
    '''
    #plotar arestas de T
    nx.draw_networkx_labels(T, pos, labels=dist)
    nx.draw_networkx_edges(T,pos)
    plt.show()
    #plt.close()
    #FIM TESTE 2

time = 0
P = {}
main()