import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_value_only(self):
        node = LeafNode(None, "happy value time lawl")
        self.assertEqual(node.to_html(), "happy value time lawl")
    
    def test_leaf_with_props(self):
        node = LeafNode("test_tag", "test_value", {"prop1": "value1", "prop2": "value2", "prop3": "value3"})
        self.assertEqual(node.to_html(), '<test_tag prop1="value1" prop2="value2" prop3="value3">test_value</test_tag>')

    def test_leaf_value_error(self):
        node = LeafNode("bad", None)
        with self.assertRaises(ValueError) as context:
            print(node.to_html())
        
        self.assertEqual(str(context.exception), "Leaf node must have a value")
    
    def test_img_leaf(self):
        node = LeafNode("img", "")
        self.assertEqual(node.to_html(), "<img />")