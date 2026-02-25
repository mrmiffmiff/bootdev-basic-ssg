import os
from blocktype import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    full_from_path = os.path.join(root, from_path)
    if not os.path.isfile(full_from_path):
        raise FileNotFoundError("From path doesn't exist or isn't a file")
    from_file = open(full_from_path)
    md = from_file.read()
    from_file.close()
    final_node = markdown_to_html_node(md)
    content = final_node.to_html()
    title = extract_title(md)
    full_template_path = os.path.join(root, template_path)
    template_file = open(full_template_path)
    surrounds = template_file.read()
    template_file.close()
    surrounds_with_title = surrounds.replace("{{ Title }}", title, 1)
    final_html = surrounds_with_title.replace("{{ Content }}", content, 1)
    full_dest_path = os.path.join(root, dest_path)
    dest_directory = os.path.dirname(full_dest_path)
    if not os.path.exists(dest_directory):
        os.mkdir(dest_directory)
    gen_file = open(full_dest_path, mode='w')
    gen_file.write(final_html)
    gen_file.close()

