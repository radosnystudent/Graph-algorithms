def find_path(path, v, temp):
    if path[v] == -1:
        temp.append(v+1)
        return temp
    find_path(path,path[v], temp)
    temp.append(v+1)
    return temp

def which_one(weights):
    if any(w < 0 for w in weights):
        return 'Bellman-Ford'
    else:
        return 'Dijkstra'

def Dijksra_vs_Bellman_Ford(graph, start, vertices, weights):
    distance = [float('Inf') for v in range(len(vertices))]
    distance[start] = 0
    path = [-1 for _ in range(len(vertices))]

    which = which_one(weights)
    
    for i in range(len(vertices)-1):
        for u, item in graph.items():
            for v,w in item.items():
                if distance[u] + w < distance[v] and which == 'Bellman-Ford':
                    distance[v] = distance[u] + w
                    path[v] = u
                elif distance[u] + w < distance[v] and w>=0 and which == 'Dijkstra':
                    distance[v] = distance[u] + w
                    path[v] = u

    if which == 'Bellman-Ford':          
        for u, item in graph.items():
            for v,w in item.items():
                if distance[u] + w < distance[v]:
                    print(f'Sa wagi ujemne. Korzystam z algorytmu Bellmana-Forda.')
                    print(f'Jest ujemny cykl. Nie ma rozwiazania.')
                    return which, None, None
    return which, distance, path

def unpack(string):
    return ' '.join(map(str, string))

def create_graph(matrix):
    graph={}

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

    return graph


def main(filename):
    matrix = list()
    
    with open(filename) as file:
        for line in file:
            matrix.append(list(map(str,line.split())))
            
    weights = [int(matrix[i][j]) for i in range(len(matrix[0])) \
               for j in range(len(matrix[0])) if matrix[i][j] != '-']
    vertices = [i for i in range(0,len(matrix[0]))]

    graph = create_graph(matrix)
    
    which, result, paths = Dijksra_vs_Bellman_Ford(graph, 0, vertices, weights)

    if which == 'Bellman-Ford':  
        if result != None and paths != None:
            print('Sa wagi ujemne. Korzystam z algorytmu Bellmana-Forda.')
            print('Najkrotsza sciezka z 1 do:')
            for i in range(len(vertices)):
                actual_path = list()
                actual_path = find_path(paths,i,actual_path)
                print(f'{i+1} : {unpack(actual_path)} ma dlugosc {result[i]}')
    else:
        print(f'Wagi sa dodatnie. Korzystam z algorytmu Dijkstry.')
        print(f'Najkrotsza sciezka z 1 do:')
        for i in range(len(vertices)):
            actual_path = list()
            actual_path = find_path(paths,i,actual_path)
            print(f'{i+1} : {unpack(actual_path)} ma dlugosc {result[i]}')


if __name__ == '__main__':
    filenames = ["files/MatrixPaths1.txt", "files/MatrixPaths2.txt", "files/MatrixPaths3.txt"]
    main(filenames[0])
