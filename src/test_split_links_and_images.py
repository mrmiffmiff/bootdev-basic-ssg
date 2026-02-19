import unittest
from textnode import TextNode, TextType
from split_links_and_images import split_nodes_image, split_nodes_link

class TestSplitLinksAndImages(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        node2 = TextNode(
            " and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node1 = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        node2 = TextNode(
            " and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_disallow_in_code(self):
        old = [
            TextNode("this would be [a link](https://www.example.com), but it's code", TextType.CODE),
            TextNode("this would be ![an image](https://i.example.com/555), but it's code", TextType.CODE)
        ]
        new = split_nodes_link(split_nodes_image(old))
        self.assertListEqual(old, new)

    def test_allow_bold_italic_composed(self):
        old = [
            TextNode("this [link](https://www.example.com) is in bold", TextType.BOLD),
            TextNode("this [link](https://www.example.com) is in italic", TextType.ITALIC),
            TextNode("this ![image](https://i.example.com/555) is in bold", TextType.BOLD),
            TextNode("this ![image](https://i.example.com/555) is in italic", TextType.ITALIC),
        ]
        expected = [
            TextNode("this ", TextType.BOLD),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" is in bold", TextType.BOLD),
            TextNode("this ", TextType.ITALIC),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" is in italic", TextType.ITALIC),
            TextNode("this ", TextType.BOLD),
            TextNode("image", TextType.IMAGE, "https://i.example.com/555"),
            TextNode(" is in bold", TextType.BOLD),
            TextNode("this ", TextType.ITALIC),
            TextNode("image", TextType.IMAGE, "https://i.example.com/555"),
            TextNode(" is in italic", TextType.ITALIC),
        ]
        actual = split_nodes_link(split_nodes_image(old))
        self.assertListEqual(expected, actual)