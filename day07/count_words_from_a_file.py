from collections import Counter

input_file = "words_and_spaces.txt"
output_file = "words_and_spaces_counted.txt"

with open(input_file, "r", encoding="utf-8") as f:
    words = f.read().lower().split()

word_counts = Counter(words)

sorted_words = sorted(word_counts.items())

with open(output_file, "w", encoding="utf-8") as f:
    for word, count in sorted_words:
        f.write(f"{word:<14}{count}\n")
