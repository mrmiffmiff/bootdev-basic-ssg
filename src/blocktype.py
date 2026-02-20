from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str):
    if bool(re.match(r"^#{1,6} .+", block)):
        return BlockType.HEADING
    if bool(re.match(r"^```\n[\s\S]*```$", block)):
        return BlockType.CODE
    if bool(re.match(r"> ?.*", block)):
        return BlockType.QUOTE
    if bool(re.fullmatch(r"(- .*\n?)+", block)):
        return BlockType.UNORDERED_LIST
    lines = block.split("\n")
    if all(re.match(rf"^{i+1}\. ", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH