import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_array(self):
        old = []
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        self.assertEqual(new, [])

    def test_empty_string(self):
        old = [TextNode("", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        self.assertEqual(new, old)

    def test_non_plain(self):
        old = [TextNode("test _test_ test", TextType.BOLD)]
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        self.assertEqual(new, old)

    def test_no_delimiter(self):
        old = [TextNode("test", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        self.assertEqual(new, old)

    def test_single_node_italic(self):
        old = [TextNode("I just _had a_ sandwich", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        first = TextNode("I just ", TextType.PLAIN)
        second = TextNode("had a", TextType.ITALIC)
        third = TextNode(" sandwich", TextType.PLAIN)
        self.assertEqual(new, [first, second, third])

    def test_single_node_bold(self):
        old = [TextNode("I just **had a** sandwich", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "**", TextType.BOLD)
        first = TextNode("I just ", TextType.PLAIN)
        second = TextNode("had a", TextType.BOLD)
        third = TextNode(" sandwich", TextType.PLAIN)
        self.assertEqual(new, [first, second, third])

    def test_single_node_code(self):
        old = [TextNode("I just `had a` sandwich", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "`", TextType.CODE)
        first = TextNode("I just ", TextType.PLAIN)
        second = TextNode("had a", TextType.CODE)
        third = TextNode(" sandwich", TextType.PLAIN)
        self.assertEqual(new, [first, second, third])

    def test_wrapping_delimiter(self):
        old = [TextNode("_I just had a sandwich_", TextType.PLAIN)]
        new = split_nodes_delimiter(old, "_", TextType.ITALIC)
        first = TextNode("", TextType.PLAIN)
        second = TextNode("I just had a sandwich", TextType.ITALIC)
        third = TextNode("", TextType.PLAIN)
        self.assertEqual(new, [first, second, third])

    def test_multiple_nodes(self):
        old_first = TextNode("I just _had a_ sandwich", TextType.PLAIN)
        old_second = TextNode("It was _no ordinary_ sandwich", TextType.PLAIN)
        old_third = TextNode("It was the _tastiest_ sandwich", TextType.BOLD) # Make sure this still isn't parsed at all
        old_fourth = TextNode("in **the** sea", TextType.PLAIN) # Make sure this still doesn't delimit something else
        new = split_nodes_delimiter([old_first, old_second, old_third, old_fourth], "_", TextType.ITALIC)
        expected = [TextNode("I just ", TextType.PLAIN),
                    TextNode("had a", TextType.ITALIC),
                    TextNode(" sandwich", TextType.PLAIN),
                    TextNode("It was ", TextType.PLAIN),
                    TextNode("no ordinary", TextType.ITALIC),
                    TextNode(" sandwich", TextType.PLAIN),
                    TextNode("It was the _tastiest_ sandwich", TextType.BOLD),
                    TextNode("in **the** sea", TextType.PLAIN)
                    ]
        self.assertEqual(new, expected)
