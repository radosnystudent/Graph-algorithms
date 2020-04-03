class Kuhn_Munkers:

    def __init__(self):
        self.edges = list()
        self.m_x = list()
        self.m_y = list()
        self.procedure_status = False
        self.S = list()
        self.T = list()
        self.p = list()
        self.NS = list()
        self.lx = list()
        self.ly = list()

    def munkers(self, matrix):
        vertices_x = [i for i in range(len(matrix))]
        self.lx = [-100 for _ in vertices_x]
        self.ly = [0 for _ in vertices_x]
        for x in range(len(vertices_x)):
            for y in range(len(vertices_x)):
                self.lx[x] = max(matrix[y][x],self.lx[x])

        next_x = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == self.lx[j] + self.ly[i]:
                    next_x[j].append(i)
        

        while True:

            if self.hungarian(vertices_x, next_x):
                break
            else:
                temp = [z for z in vertices_x if z not in self.T]
                q = None
                for x in self.NS:
                    for y in temp:
                        if q is None:
                            q = self.lx[x] + self.ly[y] - matrix[y][x]
                        else:
                            q = min(self.lx[x] + self.ly[y] - matrix[y][x], q)
                print(f'Modyikujemy etykiety: q = {q}')

                for i in self.NS:
                    self.lx[i] -= q
                for i in self.T:
                    self.ly[i] += q

                next_x = list()
                next_x = [[] for i in range(len(matrix))]
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[i][j] == self.lx[j] + self.ly[i]:
                           next_x[j].append(i)

    def hungarian(self, vertices_x, next_x):
        self.p = [None for _ in range(len(vertices_x))]

        flag = True

        while len(self.edges) != len(vertices_x) and flag is True:
            self.S = list()
            self.T = list()
            self.NS = list()

            u = [item for item in vertices_x if item not in self.m_x].pop(0)

            self.S.append(u)
            self.procedure_status = False

            while flag is True and self.procedure_status is False:
                x = self.S.pop(0)
                self.NS.append(x)
                for y in next_x[x]:
                    if y not in self.T:
                        self.T.append(y)
                        self.p[y] = x
                        if y not in self.m_y:

                            self.extend(y,u)
                            print(f'Znalezlismy ścieżkę M-zasilona. {self.unpack()}')
                            break
                        else:
                            for v in vertices_x:
                                if [v,y] in self.edges:
                                    self.S.append(v)
                                    break
                if not self.S and self.procedure_status is False:
                    flag = False
                    
        if len(self.edges) == len(vertices_x):
            print(f'Znalezlismy skojarzenie nasycajace zbior X:\n{self.unpack()}')
            return True
        else:
            return False

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
        return None

    def extend(self, y, u):
        while True:
            if self.p[y] == u:
                self.edges.append([self.p[y],y])
                self.m_x.append(self.p[y])
                self.m_y.append(y)
                break
            else:
                w = self.find_vertex(self.p[y])

                self.edges.remove([self.p[y],w])
                self.m_x.remove(self.p[y])
                self.m_y.remove(w)
                self.m_x.append(self.p[y])
                self.m_y.append(y)
                self.edges.append([self.p[y],y])
                y = w

        self.procedure_status = True


if __name__ == '__main__':
        
    matrix = list()
    with open('files/Tasks.txt') as file:
        for line in file:
            matrix.append(list(map(int,line.split())))

    K = Kuhn_Munkers()

    K.munkers(matrix)

