import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode(None, None, None, None)
        props_string = node.props_to_html()
        self.assertEqual(props_string, "")
    
    def test_props_with_repr(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com",
            "target": "_blank",
            "arbitrary_prop": "arbitrary_value"
        })
        props_string = node.props_to_html()
        self.assertEqual(props_string, ' href="https://www.google.com" target="_blank" arbitrary_prop="arbitrary_value"')
        self.assertEqual(repr(node), 'Props:  href="https://www.google.com" target="_blank" arbitrary_prop="arbitrary_value"')
    
    def test_empty_repr(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "")
    
    def test_tag_repr(self):
        node = HTMLNode("test_tag")
        self.assertEqual(repr(node), "Tag: test_tag ")
    
    def test_value_repr(self): 
        node = HTMLNode(None, "test_value")
        self.assertEqual(repr(node), "Value: test_value ")

    def test_child_repr(self):
        child1 = HTMLNode("tag1")
        child2 = HTMLNode("tag2")
        parent = HTMLNode(None, None, [child1, child2])
        self.assertEqual(repr(parent), "Children: Tag: tag1  Tag: tag2  ")
