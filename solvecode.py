import math

class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, a, b):
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
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            a = self.find(parent, s)
            b = self.find(parent, d)
            if a != b:
                e += 1
                krusk.append([s, d, w])
                self.union(parent, rank, a, b)
        
        return krusk

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

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

def clustering_with_kruskal(zones, k):
    n = len(zones)
    graph = Graph(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(zones[i], zones[j])
            graph.addEdge(i, j, distance)
    
    mst = graph.kruskal()
    mst.sort(reverse=True, key=lambda x: x[2])
    
    for _ in range(k - 1):
        mst.pop(0)
    
    ds = Disjoint(n)
    for s, d, w in mst:
        ds.union(s, d)
    
    cluster_count = [0] * n
    for i in range(n):
        cluster_count[ds.find(i)] += 1
    
    cluster_sizes = [size for size in cluster_count if size > 0]
    return sorted(cluster_sizes, reverse=True)

def main(file_path):
    cases = parse_input(file_path)
    results = []
    
    for zones, k in cases:
        result = clustering_with_kruskal(zones, k)
        results.append(result)
    
    for result in results:
        for count in result:
            print(count)
        print()

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

if __name__ == "__main__":
    file_path = "path_to_your_file.txt"
    main(file_path)
