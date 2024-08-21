import json
import os

def split_json_file(input_file, max_size_kb=400):
    # Read the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Prepare to split the data
    output_file_base = os.path.splitext(input_file)[0]  # Base name for output files
    part_number = 1
    current_size = 0
    current_part = []

    # Convert max size from KB to bytes
    max_size_bytes = max_size_kb * 1024

    for item in data:
        item_size = len(json.dumps(item).encode('utf-8'))

        # Check if adding this item would exceed the max size
        if current_size + item_size > max_size_bytes:
            # Write current part to a new file
            output_file = f"{output_file_base}_part{part_number}.json"
            with open(output_file, 'w') as outfile:
                json.dump(current_part, outfile, indent=2)

            print(f"Created {output_file} with size {current_size / 1024:.2f} KB")

            # Start a new part
            part_number += 1
            current_part = [item]
            current_size = item_size
        else:
            # Add item to the current part
            current_part.append(item)
            current_size += item_size

    # Write the last part
    if current_part:
        output_file = f"{output_file_base}_part{part_number}.json"
        with open(output_file, 'w') as outfile:
            json.dump(current_part, outfile, indent=2)

        print(f"Created {output_file} with size {current_size / 1024:.2f} KB")

# Usage
split_json_file('input.json', max_size_kb=400)
