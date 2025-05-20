def get_valid_sequences(dna):
    import re

    raw_sequences = re.split(r'[^ACGT]+', dna.upper())

    valid_sequences = [seq for seq in raw_sequences if seq]

    valid_sequences.sort(key=len, reverse=True)

    return valid_sequences


if __name__ == '__main__':
    dna = input("Please type in a sequence: ")

    result = get_valid_sequences(dna)
    print(result)
