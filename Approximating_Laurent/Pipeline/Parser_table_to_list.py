def parse_mathjax_array_from_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        mathjax_str = file.read()

    # Remove the unnecessary parts of the MathJax string
    mathjax_str = mathjax_str.replace('$$', '').replace('\\begin\\{array\\}{|c|c|}\\hline', '').replace('\\end\\{array\\}', '').replace('\\hline','').strip()
    # Split the content by line breaks and remove the header line (\tau & \alpha\\)
    lines = mathjax_str.split('\\\\')
    data_lines = lines[1:]  # Skip the first line (header)

    # Initialize the list to store the result
    result = []

    # Process each line
    for line in data_lines:
        # Skip any \hline parts
        if line.strip() == '\\hline':
            continue
        if line.strip() == '\\end{array}':
            continue
        # Split the line by '&' to separate the columns
        columns = line.strip().split('&')
        # Convert to float and add to the result list
        result.append([float(col.strip()) for col in columns])

    return result

print(parse_mathjax_array_from_file("Pipeline/mathjax_array.txt"))
