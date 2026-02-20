def markdown_to_blocks(markdown: str):
    return [x.strip() for x in markdown.split("\n\n") if x.strip()]