from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    heading = blocks[0].split("\n")[0]
    if not heading.startswith("# "):
        raise ValueError("Markdown should start with h1 header")
    return heading[2:].strip()