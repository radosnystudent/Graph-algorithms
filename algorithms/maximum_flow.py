def BFS(matrix : list, source : int, sink : int, parent : list) -> bool:
    visited, stack = [], [source]
    visited.append(source)
    
    while stack:
        v = stack.pop(0)

        for index, value in enumerate(matrix[v]):
            if index not in visited and value > 0:
                stack.append(index)
                visited.append(index)
                parent[index] = v

    if sink in visited:
        return True
    return False


def DFS(matrix : list, start : int) -> list:
    visited, stack, result = [], [start], []

    while stack:
        v = stack.pop(0)
        if v not in visited:
            visited.append(v)
            result.append(v+1)
            for u in matrix[v]:
                if u not in visited:
                    stack = [u] + stack
    return result


def MaxFlow_MinCut(matrix : list, n : int, source : int, sink : int) -> int:
    def unpack(arr : list) -> str:
        return ' '.join(map(str,arr))

    parent = [float('Inf') for _ in range(n)]
    max_flow = 0
    augmenting_paths = list()
    ind = 0

    while BFS(matrix, source, sink, parent):
        flow_on_path = float('Inf')
        t = sink
        augmenting_paths.append(list())

        while t != source:
            flow_on_path = min(flow_on_path, matrix[parent[t]][t])
            augmenting_paths[ind].append(t+1)
            t = parent[t]
        augmenting_paths[ind].append(1)
        augmenting_paths[ind].reverse()
        print(f'Ścieżka powiększająca: {unpack(augmenting_paths[ind])}. Dodajemy wartość: {flow_on_path}')
        max_flow += flow_on_path

        t = sink
        while t != source:
            u = parent[t]
            matrix[u][t] -= flow_on_path
            matrix[t][u] += flow_on_path
            t = parent[t]
        ind += 1

    mc_matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j > i and matrix[i][j] > 0:
                mc_matrix[i].append(j)
    print(f'Minimalne cięcie: {unpack(DFS(mc_matrix,0))}')

    return max_flow


if __name__ == '__main__':
    matrix = list()
    with open('MaxFlow.txt', 'r') as file:
        for line in file:
            matrix.append(list(map(int,line.replace('-','0').split())))

    print(f'Maksymalny przepływ: {MaxFlow_MinCut(matrix, len(matrix[0]), 0, len(matrix)-1)}')
