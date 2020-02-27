class BST:

    def __init__(self):
        self.root = None
        self.keys = []

    def addKey(self, key):
        if self.root is None:
            self.root = BSTnode(key)
            self.keys.append(key)
            print(f'Dodalismy: {key} , wys.: {self.height(self.root)-1}')
        else:
            self._addKey(key, self.root)

    def _addKey(self, key, node):
        if key not in self.keys:
            if key < node.key:
                if node.left is None:
                    node.left = BSTnode(key)
                    node.left.parent = node
                    self.keys.append(key)
                    print(f'Dodalismy: {key} , wys.: {self.height(self.root)-1}')
                else:
                    self._addKey(key,node.left)
            else:
                if node.right is None:
                    node.right = BSTnode(key)
                    node.right.parent = node
                    self.keys.append(key)
                    print(f'Dodalismy: {key} , wys.: {self.height(self.root)-1}')
                else:
                    self._addKey(key, node.right)
        else:
            print(f'Wierzcholek o kluczu {key} juz istnieje')

    def findNode(self, key):
        node = self.root
        while node is not None and node.key != key:
            if node.key > key:
                node = node.left
            else:
                node = node.right
        return node

    def min_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current
    
    def successor(self, node):
        if node.right is not None:
            return self.min_node(node.right)

        succ = node.parent
        while succ is not None and node == succ.right:
            node = succ
            succ = succ.parent
        return succ

    def delete(self, key):
        if key not in self.keys:
            print(f'Klucza {key} nie ma w drzewie')
        else:
            node = self.findNode(key)

            if node is None:
                return node
            else:
                self._delete(node,key)
            self.keys.remove(key)
            if self.keys:
                print(f'Usunelismy: {key} , wys.: {self.height(self.root)-1}')
            else:
                print(f'Usunelismy: {key} , drzewo zostalo calkowicie usuniete :o')

    def _delete(self, node, key):

        if node.left is None or node.right is None:
            deleted = node
        else:
            deleted = self.successor(node)

        if deleted.left is None:
            temp = deleted.right
        else:
            temp = deleted.left

        if temp is not None:
            temp.parent = deleted.parent

        if deleted.parent is None:
            self.root = temp
        else:
            if deleted == deleted.parent.left:
                deleted.parent.left = temp
            else:
                deleted.parent.right = temp

        if deleted != node:
            node.key = deleted.key

        deleted = None
        
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
        
class BSTnode:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key


if __name__ == "__main__":
    keys_insert, keys_delete = list(), list()
    with open('files/keysInsert.txt') as file:
        for line in file:
            for key in line.split():
                keys_insert.append(int(key))
    
    with open('files/keysDelete.txt') as file:
        for line in file:
            for key in line.split():
                keys_delete.append(int(key))
    
    T = BST()
    
    for key in keys_insert:
        T.addKey(key)
    print('')
    for key in keys_delete:
        T.delete(key)
