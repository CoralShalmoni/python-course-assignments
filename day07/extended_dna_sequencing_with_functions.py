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
    """Get the DNA sequence from user input (STDIN)."""
    return input("Please type in a DNA sequence:\n").strip().upper()

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
