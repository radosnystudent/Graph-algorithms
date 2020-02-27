class Node:

    def __init__(self, index):
        self.index = index
        self.root = index
        self.pred = None


class Graph:

    def __init__(self, _vertices, _edges):
        self.vertices = [Node(l) for l in range(_vertices)]
        self.edges = list()
        for edge in _edges:
            u, v = edge
            self.edges.append([self.vertices[u], self.vertices[v]])
        self.tree = [None for _ in range(_vertices)]
        self.counter = 0

    def print_tree(self):
        string = 'Krawedzie drzewa ' + str(self.counter) + ' :'

        for l in self.tree:
            if l is not None:
                string += '(' + str(self.edges[l][0].index + 1) + ', ' + str(self.edges[l][1].index + 1) + ')'
        return string
            
    def degree(self, v):
        counter = 0
        for edge in self.edges:
            if edge[0].index == v:
                counter += 1
        return counter
    
    def newRoot(self, r_new):
        r_old = r_new.root
        
        if r_old != r_new.index:
            u = None
            v = r_new.index
            
            while u != r_old:
                p = u
                u = v
                v = self.vertices[u].pred
                self.vertices[u].pred = p

        for w in self.vertices:
            if w.root == r_old:
                w.root = r_new

    def addEdge(self, edge):
        u, v = edge
        self.newRoot(v)

        v.pred = u.index

        r1 = v.root
        r2 = u.root

        for w in self.vertices:
            if w.root == r1:
                w.root = r2

    def deleteEdge(self, edge):
        u, v = edge

        if u.pred == v.index:
            v2 = u
        else:
            v2 = v

        v2.pred = None
        v2.root = v2.index

        current_pred = [v2]

        while current_pred:
            for w in self.vertices:
                if w.pred == current_pred[0].index:
                    w.root = v2.index
                    current_pred.append(w)
            del current_pred[0]
   
    def AllSpanningTrees(self):

        k = 0
        i = 0
        end = self.degree(0) + 1

        while self.tree[1] != end:
            u, v = self.edges[k]

            if u.root != v.root:
                self.addEdge(self.edges[k])
                i += 1

                self.tree[i] = k

            if self.tree[1] == end:
                break

            if i == len(self.vertices) - 1:
                self.counter += 1
                print(self.print_tree())

            if i == len(self.vertices) - 1 or k == self.edges.index(self.edges[-1]):

                if self.tree[i] == self.edges.index(self.edges[-1]):
                    self.deleteEdge(self.edges[-1])
                    i -= 1
                self.deleteEdge(self.edges[self.tree[i]])
                k = self.tree[i] + 1
                i -= 1
            else:
                k += 1


if __name__ == '__main__':
    matrix = []
    with open('files/Trees.txt') as file:
        for line in file:
            matrix.append(list(map(int, line.split())))

    vertices = len(matrix)
    edges = list()
    
    for i in range(vertices):
        for j in range(vertices):
            if j > i and matrix[i][j] != 0:
                edges.append([i, j])

    G = Graph(vertices, edges)

    G.AllSpanningTrees()
