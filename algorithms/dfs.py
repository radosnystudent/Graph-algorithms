"""
Program znajduje wszystkie składowe spójności używając algorytmu DFS
"""

def DFS(graph, start_vertex):
    visited, my_stack, result = [], [start_vertex], []
    
    while my_stack:
        vertex = my_stack.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            result.append(vertex)
            for v in graph[vertex]:
                if v not in visited:
                    my_stack = [v] + my_stack

    return result


def check_dfs(G, vertexes):
    iterator = 0
    consist_comp = []
    graph = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 1:
                graph[i].append(j)

    """
    Używając algorytmu DFS znajdujemy kolejne składowe spójności w
    zadanym grafie - każde przejście algorytmu DFS znajduje jedną składową,
    następnie z listy wszystkich wierzchołków usuwane są te, które znalazły się
    w składowej, a na pozostałych zapuszczony zostaje ponownie DFS. 
    Powtarzane jest to tak długo dopóki lista wierzchołków nie jest pusta.
    """
    while vertexes:
        result = DFS(graph,vertexes[0])
        consist_comp.append(result)
        for vertex in result:
            vertexes.remove(vertex)
    return consist_comp
 

def print_list(array):
    return ', '.join(map(str,array))


if __name__ == "__main__":
    graph=[]
    with open("files/matrixDFS.txt") as file:
        for line in file:
            graph.append(list(map(int,line.split())))

    vertexes = [i for i in range(len(graph))]
    result = check_dfs(graph,vertexes)
    all_vertexes = sum(result, [])
    
    print(f'Wierzcholki w kolejnosci ich rozpatrywania:\n{print_list(all_vertexes)}')
    print(f'Liczba skladowych spojnosci: {len(result)}')
    print(f'Kolejne skladowe:')
    for consist_comp in result:
        print(print_list(consist_comp))
