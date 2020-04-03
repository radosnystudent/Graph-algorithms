class Hamilton:

    def __init__(self, file):
        self.matrix, self.graph, self.vertices = self.read_file(file)

    def read_file(self, file):
        matrix = list()
        graph = dict()
        with open(file) as file:
            for line in file:
                matrix.append(list(map(int,line.split())))
        vertices = len(matrix)

        for i in range(vertices):
            for j in range(vertices):
                if matrix[i][j] != 0:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]

        return matrix, graph, vertices

    def unpack(self, arr):
        string = ''
        for v in arr:
            string += str(v+1) + ' '
        return string

    def Solution(self):
        v = 0
        S = list()
        S.append(v)
        u = self.graph.get(v,None)[0]

        while S:
           
            S.append(u)
            if S:
                print(f'{self.unpack(S)}')
            if len(S) == self.vertices and self.matrix[u][v] == 1:
                print(f'CYKL HAMILTONA: {self.unpack(S+[v])}')
                
            if len([item for item in self.graph.get(u,None) if item not in S]):
                temp = [item for item in self.graph.get(u,None) if item not in S]
                u = temp[0]
            else:
                check = True
                while S and check:
                    S.remove(u)
                    if S:
                        print(f'{self.unpack(S)}')
                        w = S[-1]
                        temp = [item for item in self.graph.get(w,None) if item not in S]
                        if u in temp and u != temp[-1]:
                            u = temp[temp.index(u)+1]
                            check = False
                            break
                        else:
                            u = w


if __name__ == '__main__':
    H = Hamilton('files/Hamilton.txt')
    H.Solution()
