from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict | None = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        representation = ""
        if self.tag:
            representation += f"Tag: {self.tag} "
        if self.value:
            representation += f"Value: {self.value} "
        if self.props:
            representation += f"Props: {self.props_to_html()}"
        return representation
    