from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict | None = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Nodes expected to have a tag")
        if not self.children:
            raise ValueError("Parent nodes expected to have at least one child")
        html_rep = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_rep += child.to_html()
        html_rep += f"</{self.tag}>"
        return html_rep