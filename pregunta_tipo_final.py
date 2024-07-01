
'''
- la primera linea es T
- las lineas con 3 numeros son un grafo (x,y,z) 
x=nodoinicio, y = nododestino z = peso. 
- en la linea siguiente de una con 3 elementos se almacena el valor de K 

Nota: falta mejorar :c
el out put no aprece idk
'''

import math

#leer el txt
def read_txt(file):
    with open(file, 'r') as file:
        lines = file.readlines()

    T = int(lines[0]) #cantidad de casos
    index = 1
    grafos = []
    #linea 0 -> T
    #linea 1 -> N
    #linea 2... -> (x,y,z)
    #linea 3 -> grupos

    for _ in range(T):
        #N = nodos / index = 1
        N = int(lines[index]) #se le asigna al entero de linea 1
        index +=1 #leer linea 2 en adelante
        zonas_peligrosas = []

        for _ in range(N):
            x, y, z = map(int, lines[index].split())
            zonas_peligrosas.append((x,y,z)) 
            index += 1 #paso a siguiente linea
        k = int(lines[index]) #lee linea despues de T
        index += 1
        grafos.append((zonas_peligrosas, k))

    return grafos


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, a, b): #nodo a y nodo b
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1

    def kruskal(self):
        krusk = []
        parent = []
        rank = []
        i = 0
        e = 0

        #ordenar nodos por peso
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

        return krusk

class Disjoint:
    def __init__(self, n):
        self.parent = [-1] * n
    
    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return
        if self.parent[a_root] < self.parent[b_root]:
            self.parent[a_root] += self.parent[b_root]
            self.parent[b_root] = a_root
        else:
            self.parent[b_root] += self.parent[a_root]
            self.parent[a_root] = b_root


#determina la distancia euclidiana para cada zona ya que esta en coordenadas :)
def distancia(a_,b_):
    return math.sqrt(sum((a-b)** 2 for a,b in zip(a_,b_)))

def equipos(zonas_peligrosas, k):
    n = len(zonas_peligrosas)
    graph = Graph(n)

    for i in range(n):
        for j in range(i+1, n):
            #D = distancias
            D = distancia(zonas_peligrosas[i], zonas_peligrosas[j])
            graph.add_edge(i,j, D)

        mst = graph.kruskal() #camino minimo
        mst.sort(reverse=True, key=lambda x: x[2])

        for _ in range(k-1):
            mst.pop(0)

        distances = Disjoint(n)
        for s, d, w in mst:
            distances.union(s,d) #uniendo distancias no conectadas
            
        contador = [0]*n
        for i in range(n):
            contador[distances.find(i)] + 1

        tam = [size for size in contador if size >0]
        return sorted(tam, reverse=True)
    
    def solve(file_path):
        cases = read_txt(file_path)
        results = []
        
        for zones, k in cases:
            result = equipos(zonas_peligrosas, k)
            results.append(result)
        
        for result in results:
            for count in result:
                print(count)
            print()

info  = "linternas.txt"
Graph.solve(info)