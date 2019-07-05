from rb_tree import rb_tree_map
import unittest

class test(unittest.TestCase):

    def test1(self):
        m = rb_tree_map()
        m.put(10, 'marth')
        m.put(0, 'fox')
        m.put(50, 'peach')
        m.put(40, 'samus')
        m.put(70, 'falco')
        #     10
        #   0   50
        #     40  70
        self.assertEqual(m.root.color, 'black')
        self.assertEqual(5, len(m))
        self.assertEqual('peach', m.root.right.entry.value)
        self.assertEqual('fox', m.root.left.entry.value)
        self.assertEqual('falco', m.root.right.right.entry.value)

        #remove node
        old = m.remove(50) #should promote 40 up

        #self.assertEqual(40, m.root.right.left.parent.entry.key)
        self.assertEqual(4, len(m))
        self.assertEqual('peach', old)
        self.assertEqual('samus', m.root.right.entry.value)
        self.assertEqual('falco', m.root.right.right.entry.value)
        self.assertIsNone(m.root.right.right.right.entry) # is dummy node
        self.assertIsNone(m.root.right.left.entry) # is dummy node

        #all works yay
    '''
    def test2(self):
        m = rb_tree_map()
        m.put(7, 7)
        m.put(9, 9)
        m.put(10,10)
        #  7
        #   9
        #    10
        self.assertEqual(7, m.root.left.parent.entry.key)
        m.remove(9)
        self.assertEqual(10, m.root.right.entry.key)
        m.remove(10)
        self.assertIsNone(m.root.right.entry)
    '''
    def testReid(self):
        m = rb_tree_map()
        self.assertIsNone(m.get(9))
        m.put(9, 'marth')
        self.assertEqual(1, len(m))
        m.remove(9)
        self.assertIsNone(m.get(9))
    
    def test_restsructure(self):
        m = rb_tree_map()
        m.put(1,1)
        m.put(2,2)
        m.put(3,3)
        self.assertTrue(True)
        #rendered useless now that fixing double red is added
        '''
        m._restructure(m.root.right.right)
        self.assertEqual(m.root.entry.key, 2)
        self.assertIsNone(m.root.parent)
        self.assertEqual(m.root.left.entry.key, 1)
        self.assertTrue(m.is_leaf(m.root.right.right))
        '''
    def test_ghetto_iterators(self):
        m = rb_tree_map()
        m.put(50, 50)
        m.put(0, 0)
        m.put(100, 100)
        m.remove(100)
        self.assertEqual(len(m.keys), 2)

    def test_fix_double_red(self):
        #first check condition where uncle is red and double red arises
        m = rb_tree_map()
        m.put(50, 50)
        m.put(0, 0)
        m.put(100, 100)
        self.assertEqual('red', m.root.right.color)
        self.assertEqual('red', m.root.left.color)
        #print(m.root.left.color)
        m.put(500, 500)
        self.assertEqual('black', m.root.color)
        self.assertEqual('black', m.root.right.color)
        self.assertEqual('black', m.root.left.color)
        self.assertEqual('red', m.root.right.right.color)
        #print(m.root.left.color)

        #check condition where trinode restructure occurs
        m = rb_tree_map()
        m.put(0, 0)
        m.put(50, 50)
        m.put(100, 100)
        self.assertEqual(m.root.entry.key, 50)
        self.assertEqual(m.root.color, 'black')
        self.assertEqual(m.root.left.color, 'red')
        self.assertEqual(m.root.right.color, 'red')
    
    def test_rotate(self):
        m = rb_tree_map()
        m.put(1,1)
        m.put(3,3)
        m._rotate(m.root.right)
        self.assertEqual(3, m.root.entry.key)






        

if __name__ == "__main__":
    unittest.main()