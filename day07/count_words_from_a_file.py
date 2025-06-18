from collections import Counter

# Ask user for filenames
input_file = input("Enter the input filename (e.g., words_and_spaces.txt): ")
output_file = input("Enter the output filename (e.g., words_and_spaces_counted.txt): ")

# Read and process the input file
with open(input_file, "r", encoding="utf-8") as f:
    words = f.read().lower().split()

# Count the words
word_counts = Counter(words)

# Sort words alphabetically
sorted_words = sorted(word_counts.items())

# Write results to the output file
with open(output_file, "w", encoding="utf-8") as f:
    for word, count in sorted_words:
        f.write(f"{word:<14}{count}\n")

print(f"Word counts written to {output_file}")
