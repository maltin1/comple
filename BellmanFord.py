
'''NOTACION:

N = nodes
w = weighted
v = visited
u = unvisited :)    

'''

class graph:
    
    def __init__(self, nodes):
        self.N = nodes
        self.graph = []
        
        #añadir conexiones al grafo
    def add_edges(self, u, v, w):
        self.graph.append([u,v,w])
        
    def show_array(self, dist):
        print("Distancia del nodo al inicio")
        for i in range(self.N):
            print("{0} -> {1}".format(i,dist[i])) 

    def bellmanford(self, source):
        #la distancia de los nodos empieza por infinito en un array de la longitud de la canitdad de nodos
        D = [float("inf")] * self.N
        #la distancia del nodo fuente empieza por 0
        D[source] = 0

        #ETAPA DE RELAJACIÓN
        # "_" significa para cualquier caracter

        for _ in range(self.N -1):
            for u,v,w in self.graph:
                if D[u] != float('inf') and D[u] + w < D[v]:
                    D[v] = D[u] + w
                    
        for u,v,w in self.graph:
            if D[u] != float('inf') and D[u] + w < D[v]:
                print("Grafo tiene un ciclo de pesos negativos")
                return
            
        self.show_array(D)

g = graph(5)
g.add_edges(0, 1, -1)
g.add_edges(0, 2, 4)
g.add_edges(1, 2, 3)
g.add_edges(1, 3, 2)
g.add_edges(1, 4, 2)
g.add_edges(3, 2, 5)
g.add_edges(3, 1, 1)
g.add_edges(4, 3, -3)

g.bellmanford(0)
