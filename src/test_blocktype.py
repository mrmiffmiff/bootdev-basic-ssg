import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading_1(self):
        self.assertEqual(block_to_block_type("# heading 1 test"), BlockType.HEADING)
    def test_heading_2(self):
        self.assertEqual(block_to_block_type("## heading 2 test"), BlockType.HEADING)
    def test_heading_3(self):
        self.assertEqual(block_to_block_type("### heading 3 test"), BlockType.HEADING)
    def test_heading_4(self):
        self.assertEqual(block_to_block_type("#### heading 4 test"), BlockType.HEADING)
    def test_heading_5(self):
        self.assertEqual(block_to_block_type("##### heading 5 test"), BlockType.HEADING)
    def test_heading_6(self):
        self.assertEqual(block_to_block_type("###### heading 6 test"), BlockType.HEADING)

    def test_fake_heading_7(self):
        self.assertEqual(block_to_block_type('####### "heading" 7 test'), BlockType.PARAGRAPH)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode block test```"), BlockType.CODE)

    def test_quote_block_space(self):
        self.assertEqual(block_to_block_type("> quote block with space"), BlockType.QUOTE)
    def test_quote_block_no_space(self):
        self.assertEqual(block_to_block_type(">quote block no space"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- unordered list line\n- unordered list line 2\n- unordered list line 3"), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. ordered list line 1\n2. ordered list line 2\n3. ordered list line 3"), BlockType.ORDERED_LIST)
    
    def test_regular_text(self):
        self.assertEqual(block_to_block_type("random text blocks \n lol have some fun\nyay"), BlockType.PARAGRAPH)