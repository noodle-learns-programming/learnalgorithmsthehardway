class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is None:
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if node.r is None:
                node.r = Node(val)
            else:
                self._add(val, node.r)

    def printTree(self):
        node = self.getRoot()
        self._printTree(node)

    def _printTree(self, node):
        if node is None:
            return
        print node.v
        self._printTree(node.l)
        self._printTree(node.r)
    def find(self, val):
        root = self.getRoot()
        if root is None:
            return None
        return self._find(root, val)

    def _find(self, node, val):
        if val == node.v:
            return node
        if val < node.v and node.l != None:
            return self._find(node.l, val)
        elif node.r != None:
            return self._find(node.r, val)
        return None



tree = Tree()
tree.add(2)
tree.add(1)
tree.add(3)
tree.printTree()
print '--------------------------------------------'
print tree.find(3)
        
