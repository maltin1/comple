
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
        cases.append((N, zones, k))
    
    return T, cases

def a(file_path):
    T, cases = parse_input(file_path)
    
    print(T)
    for N, zones, k in cases:
        print(N)
        for zone in zones:
            print(' '.join(map(str, zone)))
        print(k)


file_path = "linternas.txt"  # Reemplaza esto con la ruta a tu archivo
a(file_path)
