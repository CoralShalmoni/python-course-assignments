def get_clean_sequences(dna, valid_bases="ACTG"):
    """Split DNA sequence into clean sub-sequences of valid bases only."""
    current = ""
    sequences = []

    for char in dna:
        if char in valid_bases:
            current += char
        else:
            if current:
                sequences.append(current)
                current = ""
    if current:
        sequences.append(current)

    return sequences

def sort_sequences_by_length(sequences):
    """Sort sequences by descending length."""
    return sorted(sequences, key=len, reverse=True)

def get_input_sequence():
    """Get the DNA sequence from user input or file."""
    choice = input("Type '1' to enter DNA sequence manually, '2' to load from file: ").strip()
    if choice == '1':
        return input("Please type in a DNA sequence:\n").strip().upper()
    elif choice == '2':
        filename = input("Enter the filename containing the DNA sequence: ").strip()
        try:
            with open(filename, "r") as f:
                # Read all lines, join and clean whitespace/newlines
                return "".join(line.strip() for line in f).upper()
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please try again.")
            return get_input_sequence()
    else:
        print("Invalid choice. Please try again.")
        return get_input_sequence()

def print_sequences(sequences):
    """Print sorted DNA sequences."""
    print("Sorted DNA sub-sequences (longest to shortest):")
    for seq in sequences:
        print(seq)

def main():
    dna = get_input_sequence()
    clean_seqs = get_clean_sequences(dna)
    sorted_seqs = sort_sequences_by_length(clean_seqs)
    print_sequences(sorted_seqs)

if __name__ == "__main__":
    main()
