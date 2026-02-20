import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

            blocks = markdown_to_blocks(md)
            self.assertListEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_more_markdown_to_blocks(self):
              md = """
# Heading

Did you ever hear the
Tragedy of Darth Plagueis the Wise?

I thought not. It's not a story the Jedi would tell you. It's a Sith Legend.

Darth Plagueis was a Dark Lord of the Sith:

1. So powerful
2. So wise
3. He could influence the midichlorians

> He could create life.
"""

              blocks = markdown_to_blocks(md)
              self.assertListEqual(
                    blocks,
                    [
                          "# Heading",
                          "Did you ever hear the\nTragedy of Darth Plagueis the Wise?",
                          "I thought not. It's not a story the Jedi would tell you. It's a Sith Legend.",
                          "Darth Plagueis was a Dark Lord of the Sith:",
                          "1. So powerful\n2. So wise\n3. He could influence the midichlorians",
                          "> He could create life.",
                    ],
              )