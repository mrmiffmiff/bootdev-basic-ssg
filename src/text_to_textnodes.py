from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_links_and_images import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str):
    starter_node = TextNode(text, TextType.PLAIN)
    bold_split_out = split_nodes_delimiter([starter_node], "**", TextType.BOLD)
    italic_split_out = split_nodes_delimiter(bold_split_out, "_", TextType.ITALIC)
    code_split_out = split_nodes_delimiter(italic_split_out, "`", TextType.CODE)
    images_split_out = split_nodes_image(code_split_out)
    links_split_out = split_nodes_link(images_split_out)
    return links_split_out