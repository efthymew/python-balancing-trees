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
        self.assertEqual(4, len(m))
        self.assertEqual('peach', old)
        self.assertEqual('samus', m.root.right.entry.value)
        self.assertEqual('falco', m.root.right.right.entry.value)
        self.assertIsNone(m.root.right.right.right.entry) # is dummy node
        self.assertIsNone(m.root.right.left.entry) # is dummy node

        #all works yay
        

if __name__ == "__main__":
    unittest.main()