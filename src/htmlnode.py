class HTMLNode:
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list["HTMLNode"] | None = None, 
                 props: dict | None = None):
           self.tag = tag
           self.value = value
           self.children = children
           self.props = props

    def to_html(self):
          raise NotImplementedError("Child classes expected to define this method for themselves.")
    
    def props_to_html(self):
        props_string = ""
        if self.props:
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
        return props_string
    
    def __repr__(self):
        representation = ""
        if self.tag:
            representation += f"Tag: {self.tag} "
        if self.value:
            representation += f"Value: {self.value} "
        if self.children:
            representation += "Children: "
            for child in self.children:
                representation += repr(child)
                representation += " "
        if self.props:
            representation += f"Props: {self.props_to_html()}"
        return representation
