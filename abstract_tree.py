class abstract_tree_map():
    def __init__(self):
        self.root = self.Node()
        #couldnt figure out __iter__ so did this instead lol
        self.entries = []
        self.keys = []
        self.values = []
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
            self.entries.append(e)
            self.keys.append(key)
            self.values.append(value)
            self._remedy_insert(node)
            # remedy node
            self.size += 1
        else:
            temp = node.entry.value
            node.entry = e
            return temp
    
    def _remedy_insert(self, node):
        pass

    def remove(self, key):
        node = self._seek(self.root, key)[0]
        if self.is_leaf(node):
            return None
        else:
            old_val = node.entry.value
            self.entries.remove(node.entry)
            self.keys.remove(key)
            self.values.remove(old_val)
            if node.left.entry != None and node.right.entry != None:
                #replace with max of left subtree and delete other node
                newNode = self.get_max_in_tree(node.left)
                node.entry = newNode.entry
                node = newNode
            if node.left.entry != None:
                child = node.left
            else:
                child = node.right
            self._remove_node(node)
            self._remedy_remove(child)
            self.size -= 1
            # remedy double black

            return old_val

    def _remedy_remove(self, node):
        pass
            
    def _remove_node(self, node):
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
                    self._link(p, node.left, True)
                else:
                    self._link(p, node.right, True)

            else:
                if node.left.entry != None:
                    self._link(p, node.left, False)
                else:
                    self._link(p, node.right, False)
                    
    # links two nodes together
    def _link(self, parent, child, right):
        child.parent = parent
        if right:
            parent.right = child
        else:
            parent.left = child
    
    def _add_node(self, n, e, p):
        n.entry = e
        if n != self.root:
            n.color = 'red'
        n.left = self.Node()
        n.left.parent = n
        n.right = self.Node()
        n.right.parent = n
        n.parent = p

    def is_leaf(self, n):
        return n.left == None and n.right == None

    def is_internal(self, node):
        return not self.is_leaf(node)

    def get_sibling(self, node):
        if node == node.parent.right:
            return node.parent.left
        else:
            return node.parent.right
    
    def get_max_in_tree(self, node):
        if self.is_leaf(node.right):
            return node
        else:
            return self.get_max_in_tree(node.right)

    def get_min_in_tree(self, node):
        if self.is_leaf(node.left):
            return node
        else:
            return self.get_min_in_tree(node.left)


    def _rotate(self, node):
        p = node.parent
        gp = p.parent
        if gp == None:
            self.root = node
            node.parent = None
        else:
            if p == gp.right:
                self._link(gp, node, True)
            else:
                self._link(gp, node, False)

        if node == p.right:
            self._link(p, node.left, True)
            self._link(node, p, False)
        else:
            self._link(p, node.right, False)
            self._link(node, p, True)
        #fixing heights
        node.height += 1
        p.height -= 1

    
    def _restructure(self, n):
        p = n.parent
        gp = p.parent
        if (n == p.left and p == gp.left) or (n == p.right and p == gp.right):
            self._rotate(p)
            return p
        else:
            self._rotate(n)
            self._rotate(n)
            return n

    def __len__(self):
        return self.size

    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
    class Node:
        def __init__(self, entry = None, parent=None, left=None, right=None, color='black', height = 0):
            self.entry = entry
            self.parent = parent
            self.left = left
            self.right = right
            self.color = color
            self.height = height