import heapq

def prim(G):
    n = len(G)
    mst_set = [False]*n
    g = [float('inf')] * n
    g[0] = 0
    parent = [-1]*n
    q = []
    heapq.heappush(q, (0,0))

    while q:
        _,u = heapq.heappop(q)
        if mst_set[u]:
            continue
        mst_set[u] = True
        for s,w in G[u]:
            if not mst_set[s] and w < g[s]:
                g[s] = w
                parent[s] = u
                heapq.heappush(q, (w,s))
    return parent

G = [[(1,4),(2,6)], #nodo 0 conectado a 1 con peso 4
     [(0,4),(2,6),(3,3),(4,4)],
     [(0,6),(1,6),(3,1)],
     [(1,3), (2,1),(4,2),(5,3)],
     [(1,4), (3,2),(5,7)],
     [(3,3), (4,7)]]

mst = prim(G)
print("MST - Prim: ", mst) 

