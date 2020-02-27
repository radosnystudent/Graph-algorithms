from random import shuffle
from random import randint
from math import log

class BST:

    def __init__(self):
        self.root = None

    def addKey(self, key):
        if self.root is None:
            self.root = BSTnode(key)
        else:
            self._addKey(key, self.root)

    def _addKey(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = BSTnode(key)
            else:
                self._addKey(key,node.left)
        else:
            if node.right is None:
                node.right = BSTnode(key)
            else:
                self._addKey(key, node.right)

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1+ max(self.height(node.left), self.height(node.right))
        
class BSTnode:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def unpack_heights(array):
    return ' '.join(map(str,array))

def average(array):
    return sum(array)/len(array)

def expect_avg(c, n):
    return (c*log(n)) - (3*c) / (2*(c-1)) * log(log(n))

if __name__ == "__main__":
    c = float(4.311)
    n = int(input('Podaj liczbe wierzcholkow: '))
    BST_numbers = int(input('Podaj liczbe drzew BST: '))

    heights = []

    for i in range(BST_numbers):
        T = BST()
        keys = []
        for k in range(n):
            keys.append(randint(1,n))
        shuffle(keys)
        for key in keys:
            T.addKey(key)
        heights.append(T.height(T.root)-1)

    print(f'Wysokosci: {unpack_heights(heights)}')
    print(f'Srednia wysokosc otrzymanych drzew: {average(heights)}')
    print(f'Srednia oczekiwana wysokosc: {round(expect_avg(c,n),2)} + O(1)')
