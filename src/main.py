from textnode import TextNode, TextType
from copy_files import copy_files
from generate_page import generate_pages_recursive

def main():
    copy_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()