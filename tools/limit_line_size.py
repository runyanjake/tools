import sys
def split_lines(input_file: str, output_file: str, max_length: int = 80) -> None
:
    """
    Splits lines in a text file such that lines exceeding max_length are broken 
    into multiple lines of max_length or less. Lines within the limit remain 
    unchanged.
    :param input_file: Path to the input text file.
    :param output_file: Path to save the processed output text file.
    :param max_length: Maximum allowed length for a line.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        result = []
        for line in lines:
            stripped_line = line.rstrip()
            while len(stripped_line) > max_length:
                result.append(stripped_line[:max_length])
                stripped_line = stripped_line[max_length:]
            if stripped_line:
                result.append(stripped_line)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(result) + "\n")
        print(f"Processed lines written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 split_long_lines.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        split_lines(input_file, output_file)
