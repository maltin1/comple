'''ALL PAIRS SHORTEST PATH'''
import numpy as np

def graph(file):
    #lectura
    with open(file, 'r') as file:
        lines = file.readlines()

    #asignacion
    edges = []
    for line in lines:
        edges.append(list(map(int, line.split())))

    return edges

#n = nodos totales
def create_matrix(edges, n):
    inf = float('inf')
    matrix = np.full((n,n), inf)

    #nodos iguales con distancia 0
    for i in range(n):
        matrix[i][i] = 0

    for edge in edges:
        u,v,w = edge
        #en la matriz solo se presentan los pesos de los pares
        matrix [u][v] = w
    return matrix

def floyd_warshall(matrix):
    n = len(matrix)
    #generar copias de la matriz con las distancias
    D = matrix.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    #se toma la menor distancia
                    D[i][j] =  D[i][k] + D[k][j]
    return D

file = 'grafo.txt'
edges = graph(file)
n = max(max(edge[0], edge[1]) for edge in edges) + 1
matrix = create_matrix(edges, n)

dist = floyd_warshall(matrix)

print("ALL PAIRS SHORTEST PATH - FLOYD WARSHALL")
print(dist)