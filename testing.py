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

        self.assertEqual('black', m.root.color)
        self.assertEqual('red', m.root.right.color)

        #all works yay

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

        

if __name__ == "__main__":
    unittest.main()