def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    T = int(lines[0].strip())  # Número de grafos
    graphs = []
    k_values = []
    i = 1  # Índice para recorrer las líneas
    
    while i < len(lines):
        graph = []
        num_edges = int(lines[i].strip())  # Número de aristas en el grafo
        i += 1
        
        for _ in range(num_edges):
            x, y, z = map(int, lines[i].strip().split())
            graph.append((x, y, z))
            i += 1
        
        k = int(lines[i].strip())  # Valor de K para este grafo
        k_values.append(k)
        i += 1
        
        graphs.append(graph)
    
    return T, graphs, k_values

def sort_graphs_by_weight(graphs):
    sorted_graphs = []
    for graph in graphs:
        sorted_graph = sorted(graph, key=lambda edge: edge[2])  # Ordenar por el tercer elemento (peso)
        sorted_graphs.append(sorted_graph)
    return sorted_graphs

# Ejemplo de uso:
filename = 'graph.txt'  # Nombre del archivo
T, graphs, k_values = read_graph_from_file(filename)
sorted_graphs = sort_graphs_by_weight(graphs)

# Imprimir los grafos ordenados
for idx, graph in enumerate(sorted_graphs):
    print(f"Grafo {idx + 1}:")
    for edge in graph:
        print(edge)
    print(f"K = {k_values[idx]}")
