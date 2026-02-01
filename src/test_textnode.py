import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_dif_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_dif_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a textNode", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_same_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "test.url")
        node2 = TextNode("This is a text node", TextType.BOLD, "test.url")
        self.assertEqual(node, node2)
    
    def test_dif_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "test.url")
        node2 = TextNode("This is a text node", TextType.BOLD, "test2.url")
        self.assertNotEqual(node, node2)

    def test_one_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "test.url")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()