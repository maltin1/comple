'''FLUJO MÁXIMO'''
G = [[0, 8, 9, 5, 0, 0, 0],  # s = 0
     [0, 0, 0, 0, 6, 0, 0],  # 1
     [0, 0, 0, 7, 0, 5, 0],  # 2
     [0, 4, 0, 0, 2, 6, 0],  # 3
     [0, 0, 0, 0, 0, 4, 11], # 4
     [0, 0, 0, 0, 0, 0, 13], # 5
     [0, 0, 0, 0, 0, 0, 0]]  # t = 6

def bfs(grafo, s, t, padre):
    n = len(grafo)
    visitados = [False] * n
    cola = []
    
    # empieza el recorrido en s
    cola.append(s)
    visitados[s] = True
    
    while cola:
        x = cola.pop(0)
        for i in range(len(grafo[x])):
            if not visitados[i] and grafo[x][i] > 0:
                cola.append(i)
                visitados[i] = True
                padre[i] = x
                if i == t:
                    return True
    return False

def FordFulkerson(grafo, s, t):
    flujo = 0  # se inicia con flujo 0
    n = len(grafo)
    padre = [-1] * n

    while bfs(grafo, s, t, padre):
        camino = float('Inf')
        v = t
        
        # Encuentra la capacidad mínima en el camino encontrado por BFS
        while v != s:
            camino = min(camino, grafo[padre[v]][v])
            v = padre[v]
        
        # Actualiza las capacidades residuales de las aristas y las aristas inversas
        v = t
        while v != s:
            u = padre[v]
            grafo[u][v] -= camino
            grafo[v][u] += camino
            v = padre[v]
        
        flujo += camino

    return flujo

s = 0
t = 6
print("El flujo máximo es:", FordFulkerson(G, s, t))