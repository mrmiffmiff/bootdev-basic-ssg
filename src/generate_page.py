import os
from blocktype import markdown_to_html_node
from extract_title import extract_title

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    full_contents_path = os.path.join(root, dir_path_content)
    if not os.path.exists(full_contents_path):
        raise FileNotFoundError("Content path doesn't exist")
    full_dests_path = os.path.join(root, dest_dir_path)
    if not os.path.exists(full_dests_path):
        os.mkdir(full_dests_path)
    contents = os.listdir(full_contents_path)
    for path in contents:
        full_content_path = os.path.join(full_contents_path, path)
        rel_content_path = os.path.relpath(full_content_path, root)
        if os.path.isfile(full_content_path):
            filename = os.path.basename(full_content_path)
            filename_without_extension = filename.split(".")[0]
            html_filename = filename_without_extension + ".html"
            dest_path = os.path.join(os.path.dirname(path), html_filename)
            full_dest_path = os.path.join(full_dests_path, dest_path)
            rel_dest_path = os.path.relpath(full_dest_path, root)
            generate_page(rel_content_path, template_path, rel_dest_path, basepath)
        else:
            full_dest_path = os.path.join(full_dests_path, path)
            os.mkdir(full_dest_path)
            rel_dest_path = os.path.relpath(full_dest_path, root)
            generate_pages_recursive(rel_content_path, template_path, rel_dest_path, basepath)

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
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
    surrounds_with_content = surrounds_with_title.replace("{{ Content }}", content, 1)
    final_html = surrounds_with_content.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    full_dest_path = os.path.join(root, dest_path)
    dest_directory = os.path.dirname(full_dest_path)
    if not os.path.exists(dest_directory):
        os.mkdir(dest_directory)
    gen_file = open(full_dest_path, mode='w')
    gen_file.write(final_html)
    gen_file.close()

