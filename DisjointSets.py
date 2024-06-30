


#n = nodos
# esto funciona para grafos sin pesos :)
class Disjoint:
    def __init__(self, n):
        self.parent = [-1]*n
    
    def find(self, a):
        if self.parent[a] < 0:
            return a
        ab_root = self.find(self.parent[a])
        self.parent[a] = ab_root
        return ab_root
    
    def union(self, a,b):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return
        # cambio de ruta absoluta de a -> b para unirlos
        if self.parent[a_root] < self.parent[b_root]:
            self.parent[a_root] += self.parent[b_root]
            self.parent[b_root] = a_root

#un grafo con 6 nodos 
graph = Disjoint(6)
graph.union(0,1)
graph.union(1,2)
graph.union(3,4)
graph.union(4,5)

graph.find(4)
