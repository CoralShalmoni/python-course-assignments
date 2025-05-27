def count_digits(file_path):
    counts = {str(d): 0 for d in range(10)}

    with open(file_path, 'r') as f:
        for line in f:
            for ch in line:
                if ch.isdigit():
                    counts[ch] += 1

    return counts

def save_report(counts, output_file='report.txt'):
    with open(output_file, 'w') as f:
        for digit in sorted(counts.keys()):
            f.write(f"{digit} {counts[digit]}\n")

def main():
    input_file = 'numbers.txt'  # Your file path
    counts = count_digits(input_file)
    save_report(counts)

if __name__ == "__main__":
    main()
