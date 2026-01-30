from textnode import TextNode, TextType

def main():
    sample_node = TextNode("fun dummy text", TextType.LINK, "https://www.boot.dev")
    print(sample_node)

main()