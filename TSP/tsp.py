# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from heapq import heappop, heappush
from matplotlib import pyplot as plt
pop = heappop
push = heappush

def twice_around(G, origin = 0):
    H = nx.minimum_spanning_tree(G) # gero a mst a partir do grafo original
    H = nx.MultiGraph(H) # como somente multigrafos aceitam arestas paralelas
       
    for u,v in H.edges():
        H.add_edge(u,v)     #duplico arestas da mst
    
    euleraux = list(nx.eulerian_circuit(H, origin)) # gero um circuito euleriano
    #inicializa o grafo e cria uma lista auxiliar
    I = nx.Graph()
    aux = []
    #salva o circuito euleriano na lista auxiliar
    for u,v in euleraux: 
        aux.append(u)
        aux.append(v)
    h = []
    for i in aux: 
        if (i not in h):    # elimino repetições
            h.append(i)
    h.append(origin)
    for i in range (30):
        I.add_edge(h[i],h[i+1]) # gero grafo resultante
        I[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight'] # copiando também o peso
    
    return I
   
def calcular_peso(T): 
    peso = 0
    pesos = nx.get_edge_attributes(T, 'weight')
    for v in T.edges(): 
        peso += pesos[v]
    return peso
        
def main(): 
    #lê a matriz de adjacência e a transforma em um grafo
    A = np.loadtxt('ha30_dist.txt')
    G = nx.from_numpy_matrix(A)
    #inicializa a lista com os pesos minimos e maximos 
    min_pesos = []
    max_pesos = []
    for i in range(30):
        #para cada vertice de G, chama o algoritmo twice_aroud
        #o qual vai encontrar um ciclo Euleriano
        #e calcular os pesos entre as arestas
        H = twice_around(G, i)
        weight = calcular_peso(H)
        push(min_pesos, (weight, i))
        push(max_pesos, (-weight, i))
    #seleciona os 3 menores pesos
    print("Melhores:")
    for i in range(3): 
        peso, inicial = pop(min_pesos)
        print("Iniciando Tour de Euler em:", inicial, ", obteve peso:", peso)
    #seleciona os 3 maiores pesos
    print("Piores:")
    for i in range(3): 
        peso, inicial = pop(max_pesos)
        print("Iniciando Tour de Euler em:", inicial, ", obteve peso:", -peso)
    #desenha o grafo
    pos = nx.spring_layout(H, k = 0.35, iterations=100)
    nx.draw_networkx(H, pos)
    plt.show()

main()