import numpy as np

def dfs(G, u, t, visited):
    # Marca el nodo u como visitado
    visited[u] = True
    # Si el nodo actual es el sumidero, devolvemos el camino actual (que solo contiene el nodo t)
    if u == t:
        return [u], np.Inf
    else:
        n = len(G)
        # Recorremos todos los nodos v adyacentes a u
        for v in range(n):
            # Si hay capacidad residual positiva y v no ha sido visitado
            if G[u][v] > 0 and not visited[v]:
                # Realiza una llamada recursiva a dfs desde v
                path, mind = dfs(G, v, t, visited)
                # Si se encuentra un camino (path no es None)
                if path is not None:
                    # Devuelve el camino actual y la capacidad mínima en el camino
                    return [u] + path, min(mind, G[u][v])
        # Si no se encuentra un camino, devuelve None y 0
        return None, 0

def fordFulkerson(G, s, t):
    n = len(G)
    # Inicializa el grafo residual como una copia del grafo original
    Gres = G.copy()
    # Inicializa la matriz de flujo con ceros
    Gflow = np.zeros((n, n))
    
    while True:
        # Encuentra un camino de aumento en el grafo residual
        path, bottleneck = dfs(Gres, s, t, [False]*n)
        
        # Si no se encuentra un camino, termina el bucle
        if path is None:
            break
        
        # Ajusta las capacidades en el grafo residual y actualiza el flujo
        for i in range(1, len(path)):
            u = path[i - 1]
            v = path[i]
            # Resta la capacidad del bottleneck a la arista (u, v)
            Gres[u][v] -= bottleneck
            # Añade la capacidad del bottleneck a la arista (v, u) (capacidad residual)
            Gres[v][u] += bottleneck
            # Actualiza el flujo en la arista (u, v)
            Gflow[u][v] = Gflow[u][v] - Gflow[v][u] + bottleneck
    
    # Devuelve la matriz de flujo y el flujo máximo (la suma de los flujos salientes del nodo fuente)
    return Gflow, np.sum(Gflow[s])

# Ejemplo de uso
G = np.array([[0, 16, 13, 0, 0, 0],
              [0, 0, 10, 12, 0, 0],
              [0, 4, 0, 0, 14, 0],
              [0, 0, 9, 0, 0, 20],
              [0, 0, 0, 7, 0, 4],
              [0, 0, 0, 0, 0, 0]])

s = 0  # Nodo fuente
t = 5  # Nodo sumidero

# Ejecutar el algoritmo de Ford-Fulkerson
Gflow, max_flow = fordFulkerson(G, s, t)
print("Matriz de Flujo:")
print(Gflow)
print("Flujo Máximo:", max_flow)
