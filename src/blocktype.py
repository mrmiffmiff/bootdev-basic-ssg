from enum import Enum
import re
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from convert_node import text_node_to_html_node
from textnode import TextType, TextNode
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str):
    if bool(re.match(r"^#{1,6} .+", block)):
        return BlockType.HEADING
    if bool(re.match(r"^```\n[\s\S]*```$", block)):
        return BlockType.CODE
    if bool(re.match(r"> ?.*", block)):
        return BlockType.QUOTE
    if bool(re.fullmatch(r"(- .*\n?)+", block)):
        return BlockType.UNORDERED_LIST
    lines = block.split("\n")
    if all(re.match(rf"^{i+1}\. ", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(text_node_to_html_node, text_nodes))

def get_list_nodes(lines: list[str]):
    children = []
    for line in lines:
        in_li = text_to_children(line)
        li = ParentNode("li", in_li)
        children.append(li)
    return children

def block_to_block_node(block: str):
    match block_to_block_type(block):
        case BlockType.HEADING:
            level = block.index(' ')
            content = block[level + 1:]
            children = text_to_children(content)
            parent = ParentNode(f"h{level}", children)
            return parent
        case BlockType.CODE:
            content = block[4:-3]
            content_text_node = TextNode(content, TextType.CODE)
            content_html_node = text_node_to_html_node(content_text_node)
            parent = ParentNode("pre", [content_html_node])
            return parent
        case BlockType.QUOTE:
            start_index = 2 if block[1] == " " else 1
            content = block[start_index:]
            children = text_to_children(content)
            parent = ParentNode("blockquote", children)
            return parent
        case BlockType.UNORDERED_LIST:
            lines = block[2:].split("\n- ")
            children = get_list_nodes(lines)
            parent = ParentNode("ul", children)
            return parent
        case BlockType.ORDERED_LIST:
            lines = re.split(r"\n\d+\. ", block[3:])
            children = get_list_nodes(lines)
            parent = ParentNode("ol", children)
            return parent
        case BlockType.PARAGRAPH:
            content = block.replace("\n", " ")
            return ParentNode("p", text_to_children(content))

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_nodes.append(block_to_block_node(block))
    return ParentNode("div", block_nodes)
