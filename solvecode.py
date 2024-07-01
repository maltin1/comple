import math
from heapq import heappop, heappush

# Clase para manejar conjuntos disjuntos (Union-Find)
class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Función para leer el archivo de entrada
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    index = 0
    T = int(lines[index])
    index += 1
    cases = []
    
    for _ in range(T):
        N = int(lines[index])
        index += 1
        zones = []
        for _ in range(N):
            x, y, z = map(int, lines[index].split())
            zones.append((x, y, z))
            index += 1
        k = int(lines[index])
        index += 1
        cases.append((zones, k))
    
    return cases

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

# Función para realizar el clustering usando el algoritmo de Kruskal
def kruskal_clustering(zones, k):
    n = len(zones)
    edges = []
    # Construir todas las aristas con su distancia
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(zones[i], zones[j])
            edges.append((distance, i, j))
    
    edges.sort()  # Ordenar las aristas por distancia
    ds = DisjointSets(n)
    mst = []
    
    # Crear el MST usando el algoritmo de Kruskal
    for edge in edges:
        distance, u, v = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)
    
    # Ordenar las aristas del MST en orden descendente y eliminar las (k-1) más largas
    mst.sort(reverse=True, key=lambda x: x[0])
    
    for _ in range(k - 1):
        if mst:
            mst.pop(0)
    
    # Contar el número de zonas en cada cluster
    clusters = [0] * n
    for _, u, v in mst:
        clusters[ds.find(u)] += 1
        clusters[ds.find(v)] += 1
    
    cluster_sizes = [size for size in clusters if size > 0]
    return sorted(cluster_sizes, reverse=True)

# Función principal
def main(file_path):
    cases = parse_input(file_path)
    results = []
    
    for zones, k in cases:
        result = kruskal_clustering(zones, k)
        results.append(result)
    
    # Imprimir los resultados en el formato requerido
    for result in results:
        for count in result:
            print(count)
        print()

if __name__ == "__main__":
    file_path = "path_to_your_file.txt"  # Reemplaza esto con la ruta a tu archivo
    main(file_path)
