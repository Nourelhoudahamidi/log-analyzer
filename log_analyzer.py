def analyze_log(input_file='log.txt', output_file='rapport.txt'):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    error_count = sum('ERROR' in line for line in lines)
    warning_count = sum('WARNING' in line for line in lines)
    info_count = sum('INFO' in line for line in lines)

    with open(output_file, 'w') as report:
        report.write(f"Lignes : {line_count}\n")
        report.write(f"Mots : {word_count}\n")
        report.write(f"Caractères : {char_count}\n")
        report.write(f"ERROR : {error_count}\n")
        report.write(f"WARNING : {warning_count}\n")
        report.write(f"INFO : {info_count}\n")

if __name__ == "__main__":
    analyze_log()
