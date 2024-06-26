'''NOTA: este código aplica bellman ford pero leyenod un grafo por un txt '''
import graphviz
from graphviz import Digraph

def crear_grafo(graph_):
    graph = Digraph()
    edges = []
    with open(graph_, 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) == 3:
                u,v,w = data[0], data[1], data[2]
                graph.edge(u,v,label = w)
                edges.append((int(u), int(v), int(w)))
    
    return graph, edges

def show_graph(graph):
    graph.render('grafo', format='svg')
    graph.view()

def output(D):
    print("Distancia del nodo al inicio")
    for i in range(n):
        print("{0} -> {1}".format(i,D[i]))


def bellmanford(edges, n, source):
    #distancia de nodos = inf
    #distancia del nodo source es 0
    D = [float('inf')] * n
    D[source] = 0
    
    for _ in range(n-1):
        for u,v,w in edges:
            if D[u] != float('inf') and D[u] + w < D[v]:
                D[v] = D[u] + w
    
    for u,v,w in edges:
        if D[u] != float('inf') and D[u] + w < D[v]:
            print("Existe un ciclo negativo")
            return
    
    def output(D):
        print("Distancia del nodo al inicio")
        for i in range(len(D)):
            print("{0} -> {1}".format(i,D[i]))
    
    output(D)


n = 5
source = 0
file = 'grafo.txt'
grafo, edges = crear_grafo(file)
show_graph(grafo)
bellmanford(edges, n, source)

