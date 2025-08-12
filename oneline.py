import sys

def extract_lines_with_syntax(file_path, search_strings):
    results = {search: [] for search in search_strings}
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            for search in search_strings:
                if search in line:
                    results[search].append(line.strip())  # Remove leading/trailing whitespace
    return results

if len(sys.argv) < 3:
    print("Kullanım: python oneline.py <file_path> <search_strings>")
    sys.exit(1)

file_path = sys.argv[1]
search_strings = sys.argv[2].split(', ')

results = extract_lines_with_syntax(file_path, search_strings)

for search, lines in results.items():
    if len(lines) > 0:
        with open(f"{search}_output.txt", "a", encoding='utf-8') as txt_file:
            for line in lines:
                print(line)
                txt_file.write(line + '\n')
    else:
        print(f"No lines containing '{search}' were found in the file.")
