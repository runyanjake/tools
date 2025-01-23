import json
import sys

def pretty_print_json(input_file: str, output_file: str) -> None:
    """
    Reads a JSON file, pretty prints its content, and saves it to a new file.
    
    :param input_file: Path to the input JSON file.
    :param output_file: Path to the output file where pretty-printed JSON will be saved.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        print(f"Pretty-printed JSON has been saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_file}. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pretty_print_json.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        pretty_print_json(input_file, output_file)
