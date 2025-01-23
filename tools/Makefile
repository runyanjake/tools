INPUT_FILE=input.txt
OUTPUT_FILE=output.txt

# Remove input and output files
clean:
	rm -f $(INPUT_FILE) $(OUTPUT_FILE)

# Create input file
build:
	touch $(INPUT_FILE)

# Run pretty_print_json.py
pretty_print_json:
	@echo "Running pretty_print_json.py with $(INPUT_FILE) and $(OUTPUT_FILE)"
	python3 pretty_print_json.py $(INPUT_FILE) $(OUTPUT_FILE)

# Run limit_line_size.py
limit_line_size:
	@echo "Running limit_line_size.py with $(INPUT_FILE) and $(OUTPUT_FILE)"
	python3 limit_line_size.py $(INPUT_FILE) $(OUTPUT_FILE)

