class rb_tree_map:
    def __init__(self):
        self.root = self.Node()
        self.size = 0

    def _seek(self, n, key, last=None):
        if self.is_leaf(n):
            return n, last
        if key == n.entry.key:
            return n, last
        elif key < n.entry.key:
            return self._seek(n.left, key, n)
        else:
            return self._seek(n.right, key, n)
    
    def get(self, key):
        node = self._seek(self.root, key)[0]
        if self.is_leaf(node):
            return None
        else:
            return node.entry.value

    def put(self, key, value):
        e = self.Entry(key, value)
        node, p = self._seek(self.root, key)

        if self.is_leaf(node):
            self._add_node(node, e, p)
            # remedy node
            self.size += 1
        else:
            temp = node.entry.value
            node.entry = e
            return temp

    def remove(self, key):
        node = self._seek(self.root, key)[0]
        if self.is_leaf(node):
            return None
        else:
            old_val = node.entry.value
            if node.left.entry != None and node.right.entry != None:
                #replace with max of left subtree and delete other node
                newNode = self.get_max_in_tree(node.left)
                node.entry = newNode.entry
                node = newNode
            self.__remove_node(node)
            self.size -= 1
            # remedy double black

            return old_val
            
            

    def __remove_node(self, node):
        p = node.parent
        #breaking links
        if node == self.root:
            if node.left.entry != None:
                self.root = node.left
                node.left.parent = None
            elif node.right.entry != None:
                self.root = node.right
                node.right.parent = None
            else:
                self.root = self.Node()
        else:
            if node == p.right:
                if node.left.entry != None:
                    self.__link(p, node.left, True)
                else:
                    self.__link(p, node.right, True)

            else:
                if node.left.entry != None:
                    self.__link(p, node.left, False)
                else:
                    self.__link(p, node.right, False)
                    
    # links two nodes together
    def __link(self, parent, child, right):
        child.parent = parent
        if right:
            parent.right = child
        else:
            parent.left = child
    
    def get_max_in_tree(self, node):
        if node.right.entry == None:
            return node
        else:
            return self.get_max_in_tree(node.right)

    def get_min_in_tree(self, node):
        if node.left.entry == None:
            return node
        else:
            return self.get_min_in_tree(node.left)
    
    def is_leaf(self, n):
        return n.left == None and n.right == None

    def is_black(self, n):
        return n.color == 'black'

    def is_red(self, n):
        return n.color == 'red'
    
    def _add_node(self, n, e, p):
        n.entry = e
        if n != self.root:
            n.color = 'red'
        n.left = self.Node()
        n.left.parent = n
        n.right = self.Node()
        n.right.parent = n
        n.parent = p

    def is_internal(self, node):
        return not self.is_leaf(node)

    def get_sibling(self, node):
        if node == node.parent.right:
            return node.parent.left
        else:
            return node.parent.right

    def __len__(self):
        return self.size
    
    '''
    def __put_repair(self, node):

    def __remove_repair(self, node):
    '''
    #def __rotate(self, node):

    #def __restructure(self, node):


    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
    class Node:
        def __init__(self, entry = None, parent=None, left=None, right=None, color='black'):
            self.entry = entry
            self.parent = parent
            self.left = left
            self.right = right
            self.color = color