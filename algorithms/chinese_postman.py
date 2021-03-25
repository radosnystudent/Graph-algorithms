def return_path(path, v, temp):
    if path[v] == -1:
        temp.append(v)
        return temp
    return_path(path, path[v], temp)
    temp.append(v)
    return temp

def dijkstra(matrix, start):
    graph = {}

    for i in range(0,len(matrix[0])):
        temp = {}
        for j in range(0,len(matrix[0])):
            if matrix[i][j] != '-':
                if j not in temp:
                    temp[j] = int(matrix[i][j])
                else:
                    temp[j].append(int(matrix[i][j]))
        if i not in graph:
            graph[i] = temp
        else:
            graph[i].append(temp)
    
    distance = [float('Inf') for v in range(len(matrix))]
    distance[start] = 0
    path = [-1 for i in range(len(matrix))]
    
    for i in range(len(matrix)-1):
        for u, item in graph.items():
            for v,w in item.items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    path[v] = u
    return distance, path

def find_odds(matrix):
    degrees = [0 for _ in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != 0 and matrix[row][col].isdigit() and row != col:
                degrees[row] += 1

    odds_v = list()
    for vertex in range(len(degrees)):
        if degrees[vertex] % 2 != 0:
            odds_v.append(vertex)
    return odds_v    

def all_pairs(odds_v):
    pairs = [[odds_v[i], odds_v[j]] for i in range(len(odds_v)) for j in range(i+1, len(odds_v))]
    return pairs

def pairs_paths(odds_v, pairs, matrix):
    temp_d = list()
    temp_p = list()
    
    for odd in odds_v:
        d,p = dijkstra(matrix, odd)
        temp_d.append(d)
        temp_p.append(p)
    for pair in pairs:
        pair.append(temp_d[odds_v.index(pair[0])][pair[1]])
    sorted_pairs = sorted(pairs, key=lambda x: x[2])        

    i = 0
    check = True
    counter = [k for k in odds_v]
    winners = list()

    while counter:
        f = sorted_pairs[i]
        counter.remove(f[0])
        counter.remove(f[1])
        for j in range(len(pairs)):
            if sorted_pairs[j][0] not in f and sorted_pairs[j][1] not in f:
                counter.remove(sorted_pairs[j][0])
                counter.remove(sorted_pairs[j][1])
                winners.append(f)
                winners.append(sorted_pairs[j])
        if counter:
            counter = odds_v
            i += 1
    
    paths = list()
    for win in winners:
        temp = list()
        temp = return_path(temp_p[odds_v.index(win[0])], win[1], temp)
        paths.append(temp)
    return paths

def new_matrix(matrix, paths):
    pairs = list()
    matrix_len = len(matrix)
    for path in paths:
        for i in range(len(path) - 1):
            pairs.append([path[i], path[i + 1]])
    
    fleury = [[] for _ in range(matrix_len)]

    for i in range(matrix_len):
        for j in range(matrix_len):
            if matrix[i][j] != '-':
                if matrix[i][j] == '0':
                    fleury[i].append(0)
                else:
                    fleury[i].append(1)
                    if [i, j] in pairs or [j, i] in pairs:
                        fleury[i][j] += 1
            else:
                fleury[i].append(0)
    return fleury

def check_edge(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                return True
    return False

def bfs(matrix, start, end):
    graph = {}
    path = list()

    for i in range(len(matrix)):
        graph[i] = []
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                graph[i].append(j)
    
    visited, queue = set([start]), list([start])
    while queue:
        vertex = queue.pop(0)
        path.append(vertex)
        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    
    if end in path:
        return True
    return False

def is_bridge(matrix, v, u, path, temp):
    if matrix[v].count(0) == len(matrix[v])-1:
        matrix[v][u] -= 1
        matrix[u][v] -= 1
        path.append(v)
        return True
    else:
        matrix[v][u] -= 1
        matrix[u][v] -= 1

        if bfs(matrix, v, u):
            path.append(v)
            return True
        else:
            matrix[v][u] += 1
            matrix[u][v] += 1
            temp.append([v, u])
            return False
    return False

def fleury(new_matrix, start):
    current = start
    path, temp = list(), list()

    while check_edge(new_matrix):
        _help = False
        for u in range(len(new_matrix)):
            if new_matrix[current][u] > 0:
                if is_bridge(new_matrix,current,u,path,temp):
                    current = u
                    _help = True
            if _help:
                break
    path.append(start)
    for i in range(len(path)):
        path[i] += 1
    for i in range(len(temp)):
        for j in range(len(temp)):
            temp[i][j] += 1
    return path, temp
         
if __name__ == '__main__':
    matrix = list()

    with open('./files/Chinski.txt') as file:
        for line in file:
            matrix.append(line.split())
    odds_v = find_odds(matrix)

    if len(odds_v) <= 4:
        print(f'Liczba wierzchołków o nieparzystym stopniu: {len(odds_v)}')
        if len(odds_v) > 0:
            print(f'Wierzchołki o nieparzystym stopniu: {odds_v}')
        pairs = all_pairs (odds_v)
        paths = pairs_paths(odds_v, pairs, matrix)
        if len(paths) > 0:
            print('Najkrótsze ścieżki: ')
            for h in paths:
                print(f'{h[0]+1} do {h[-1]+1}')

        new_matrix = new_matrix(matrix, paths)
        path, temp = fleury(new_matrix, 0)
        if temp:
            print('Ignorowane krawedzie ciecia: ')
            for t in temp:
                print (t)
        print (f'Rozwiazanie problemu chinskiego listonosza: \n{path}')
    else:
        print('Brak rozwiązania. Liczba wierzchołków nieparzystych jest większa od 4.')
