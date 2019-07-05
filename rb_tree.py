from abstract_tree import abstract_tree_map
class rb_tree_map(abstract_tree_map):
    def __init__(self):
        super().__init__()
    
    def _remedy_insert(self, node):
        p = node.parent
        if p.color == 'red':
            uncle = self.get_sibling(p)
            if uncle.color == 'black':
                node = self._restructure(node)
                node.color = 'black'
                node.left.color = 'red'
                node.right.color = 'red'
            else:
                uncle.color = 'black'
                p.color = 'black'
                if p.parent != self.root:
                    p.parent.color = 'red'
                    self._remedy_insert(p.parent)

    def _remedy_remove(self, node):
        pass