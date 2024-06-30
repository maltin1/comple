
'''MST: arbol de expansion minima'''

#v = vertices
class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = []

    #s -> source
    #d -> destination
    #w -> weight
    def addEdge(self, s, d, w):
        self.graph.append([s,d,w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, a, b):
        # el nodo que es apuntado (a -> b) debe ser de mayor rango
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        #si los rangos son iguales se suma 1 al rango del nodo padre :)
        else:
            parent[b] = a
            rank[a] += 1

    def kruskal(self):
        krusk = []
        parent = []
        rank = []
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        #se repite hasta el máximo de conexiones = v-1        
        while e < self.V - 1:
            #escogemos la conexion más pequeña
            s,d,w = self.graph[i]
            i = i+1
            #buscamos el abs_root de los nodos
            a = self.find(parent, s)
            b = self.find(parent, d)

            #verificamos que no genere un ciclo
            #se añade el "camino" y se incrementa el index
            if a != b:
                e = e +1
                krusk.append([s,d,w])
                self.union(parent, rank, a, b)
        mst = 0
        print("MST-Kruskal: ")
        for s,d,w in krusk:
            mst= mst + w
            print("%d - %d: %d" % (s, d, w))

        print("Costo total: ", mst)


g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
g.kruskal()
