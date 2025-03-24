#!/usr/bin/env python3
import os

def split_examples(input_file, output_dir):
    # Read the entire file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the file contains a header and an examples marker, first isolate the examples section.
    # In this file the examples section starts after "## Examples" and then a line with "--------------------------------".
    if "## Examples" in content:
        _, examples_section = content.split("## Examples", 1)
        examples_section = examples_section.strip()
        # Optionally remove the separator line if it exists at the top:
        if examples_section.startswith('--------------------------------'):
            _, examples_section = examples_section.split('\n', 1)
    else:
        examples_section = content

    # Assuming each example is separated by one or more blank lines, split by double newline.
    examples = [ex.strip() for ex in examples_section.split("\n\n") if ex.strip()]

    # Create an output directory for the examples if it doesn't already exist.
    os.makedirs(output_dir, exist_ok=True)

    # Write each example to its own file.
    for index, example in enumerate(examples, start=1):
        filepath = os.path.join(output_dir, f'example_{index:02d}.md')
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(example)
        print(f'Created: {filepath}')

if __name__ == "__main__":
    input_file = "data/taxonomy-v2.md"
    output_dir = "examples"
    split_examples(input_file, output_dir)