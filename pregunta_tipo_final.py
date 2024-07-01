
#leer el txt
def read(file):
    with open(file, 'r') as file:
        lines = file.readline

    index = 0
    T = int(lines[index])
    index += 1
    cases = []

    for _ in range(T):
        N = int(lines[index])
        index += 1
        zones = []
        for _ in range(N):
            x,y,z = map(int, lines[index].split())
            zones.append((x,y,z))
            index += 1
        k = int(lines[index])
        index += 1
        cases.append((zones,k))

    return cases




info = "linternas.txt"
read(info)
