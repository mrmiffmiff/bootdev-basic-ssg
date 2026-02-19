from textnode import TextNode, TextType
from find_links_and_images import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type not in [TextType.PLAIN, TextType.BOLD, TextType.ITALIC]:
            new_nodes.append(node)
            continue
        new_inner_nodes = []
        images = extract_markdown_images(node.text)
        to_split = node
        for image in images:
            sections = to_split.text.split(f"![{image[0]}]({image[1]})", 1)
            new_inner_nodes.append(TextNode(sections[0], node.text_type))
            new_inner_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            to_split = TextNode(sections[1], node.text_type)
        if to_split.text != "":
            new_inner_nodes.append(to_split)
        new_nodes.extend(new_inner_nodes)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type not in [TextType.PLAIN, TextType.BOLD, TextType.ITALIC]:
            new_nodes.append(node)
            continue
        new_inner_nodes = []
        links = extract_markdown_links(node.text)
        to_split = node
        for link in links:
            sections = to_split.text.split(f"[{link[0]}]({link[1]})", 1)
            new_inner_nodes.append(TextNode(sections[0], node.text_type))
            new_inner_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            to_split = TextNode(sections[1], node.text_type)
        if to_split.text != "":
            new_inner_nodes.append(to_split)
        new_nodes.extend(new_inner_nodes)
    return new_nodes