class Hungarian:

    def __init__(self):
        self.edges = list()
        self.m_x = list()
        self.m_y = list()
        self.procedure_status = False
        self.S = list()
        self.T = list()
        self.p = list()

    def matching(self, vertices_x, next_x):

        self.p = [None for _ in range(len(vertices_x))]

        skoj = True

        while len(self.edges) != len(vertices_x) and skoj is True:
            self.S = list()
            self.T = list()
            NS = list()

            u = [item for item in vertices_x if item not in self.m_x].pop(0)

            self.S.append(u)
            self.procedure_status = False

            while skoj is True and self.procedure_status is False:
                x = self.S.pop(0)
                NS.append(x)
                for y in next_x[x]:
                    if y not in self.T:
                        self.T.append(y)
                        self.p[y] = x
                        if y not in self.m_y:
                            self.extend(y,u)
                            print(f'{self.unpack()}')
                            break
                        else:
                            for v in vertices_x:
                                if [v,y] in self.edges:
                                    self.S.append(v)
                                    break
                if not self.S and self.procedure_status is False:
                    skoj = False
                    
        if len(self.edges) == len(vertices_x):
            print(f'Znalezlismy skojarzenie nasycajace zbior X:\n{self.unpack()}')
            pass
        else:
            NS.sort()
            print(f'Nie ma skojarzenia w grafie. Dla S = ({self.print_arr(NS)}) mamy |N(S)| < |S|')
            pass

    def unpack(self):
        self.edges.sort(key=lambda x: x[0])
        string = 'Aktualne skojarzenie: '
        for edge in self.edges:
            string += '(' + str(edge[0]+1) + ',' + str(edge[1]+1) + ')'
        return string

    def find_vertex(self, x):
        for edge in self.edges:
            if x == edge[0]:
                return edge[1]
            elif x == edge[1]:
                return edge[0]
        return None

    def print_arr(self, arr):
        string = ''
        for item in arr:
            string += str(item + 1) + ' '
        return string

    def extend(self, y, u):
        temp = list()
        while True:
            if self.p[y] == u:
                self.edges.append([self.p[y],y])
                self.m_x.append(self.p[y])
                self.m_y.append(y)
                temp.append(y)
                temp.append(self.p[y])
                break
            else:
                w = self.find_vertex(self.p[y])
                self.edges.remove([self.p[y],w])
                self.m_x.remove(self.p[y])
                self.m_y.remove(w)
                self.m_x.append(self.p[y])
                self.m_y.append(y)
                self.edges.append([self.p[y],y])
                temp.append(y)
                temp.append(self.p[y])
                y = w
        temp.reverse()
        print(f'Ścieżka M-zasilona:: {self.print_arr(temp)}')
        self.procedure_status = True

if __name__ == '__main__':
    files = ['files/Matching.txt','files/Matching2.txt']
    matrix = list()
    with open(files[0]) as file:
        for line in file:
            matrix.append(list(map(int,line.split())))
    vertices = [i for i in range(len(matrix))]
    next_x = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                next_x[j].append(i)

    H = Hungarian()
    H.matching(vertices, next_x)
