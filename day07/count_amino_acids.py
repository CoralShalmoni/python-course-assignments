from collections import Counter

# Codon table (amino acid → list of codons)
codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Convert codon → amino acid
codon_to_amino = {codon: aa for aa, codons in codon_table.items() for codon in codons}

# Input file name
input_file = "dna_sequence.txt"  # or .txt, works the same

# Read file and clean up sequence
with open(input_file, "r") as f:
    sequence = "".join(
        line.strip().upper()
        for line in f
        if not line.startswith(">")
    )

# Break sequence into codons
codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]

# Translate codons into amino acids
amino_acids = [codon_to_amino.get(codon, '???') for codon in codons]

# Count valid amino acids only
counts = Counter(aa for aa in amino_acids if aa not in ('STOP', '???'))

# Print results
for aa, count in sorted(counts.items()):
    print(f"{aa:<6}: {count}")
