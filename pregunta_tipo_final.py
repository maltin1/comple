
'''
- la primera linea es T
- las lineas con 3 numeros son un grafo (x,y,z) 
x=nodoinicio, y = nododestino z = peso. 
- en la linea siguiente de una con 3 elementos se almacena el valor de K 
'''

#leer el txt
def read_txt(file):
    with open(file, 'r') as file:
        lines = file.readlines()

    T = int(lines[0].strip()) #cantidad de casos
    index = 1
    grafos = []
    #linea 0 -> T
    #linea 1 -> N
    #linea 2... -> (x,y,z)

    for _ in range(T):
        #N = nodos / index = 1
        N = int(lines[index]) #se le asigna al entero de linea 1
        index +=1 #leer linea 2 en adelante
        zonas_peligrosas = []

        for _ in range(N):
            x, y, z = map(int, lines[index])