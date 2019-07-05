from abstract_tree import abstract_tree_map
class rb_tree_map(abstract_tree_map):
    def __init__(self):
        super().__init__()
    
    def _remedy_insert(self, node):
        if self.root != node:
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
        if node.color == 'red':
            node.color = 'black'
        elif node != self.root:
            sib = self.get_sibling(node)
            if sib.entry != None and (sib.color == 'black' or sib.left.entry != None):
                self.__fix_double_black(node)
    def __fix_double_black(self, node):
        p = node.parent
        s = self.get_sibling(node)
        if s.color == 'red':
            self._rotate(s)
            s.color = 'black'
            p.color = 'red'
            self.__fix_double_black(node)
        else:
            if s.left.color =='red' or s.right.color == 'red':
                if s.left.color == 'red':
                    temp = s.left
                else:
                    temp = s.right
                m = self._restructure(temp)
                if p.color == 'red':
                    m.color = 'red'
                else:
                    m.color = 'black'
                m.left.color = 'black'
                m.right.color = 'black'
            else:
                s.color = 'red'
                if p.color == 'red':
                    p.color = 'black'
                elif p != self.root:
                    self.__fix_double_black(p)