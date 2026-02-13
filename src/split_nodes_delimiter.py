from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid Markdown Syntax")
            split_nodes = []
            for index, string in enumerate(split_text):
                new_text_type = TextType.PLAIN if index % 2 == 0 else text_type
                split_nodes.append(TextNode(string, new_text_type))
            new_nodes.extend(split_nodes)
    return new_nodes