import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as context:
            print(parent_node.to_html())
        self.assertEqual(str(context.exception), "Parent Nodes expected to have a tag")

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as context:
            print(parent_node.to_html())
        self.assertEqual(str(context.exception), "Parent nodes expected to have at least one child")

    def test_to_html_multiple_children(self):
        child1 = LeafNode("span", "child1")
        child2 = LeafNode("span", "child2")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><span>child1</span><span>child2</span></div>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"arbi": "trary"})
        self.assertEqual(parent_node.to_html(), '<div arbi="trary"><span>child</span></div>')
    
    def test_to_html_child_with_raw_text(self):
        child = LeafNode(None, "test text")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div>test text</div>")