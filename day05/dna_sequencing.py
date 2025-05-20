def get_sequences(dna):
    raw_sequences = dna.split('X')
    sequences = [seq for seq in raw_sequences if seq]
    sequences.sort(key=len, reverse=True)
    
    return sequences

if __name__ == '__main__':
    dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
    
    short_sequences = get_sequences(dna)

    print("Sorted DNA sub-sequences (longest to shortest):")
    print(short_sequences)
