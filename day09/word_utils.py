def count_words(word_list):
    """
    Count how many times each word appears in the list.

    Args:
        word_list (list of str): A list of words.

    Returns:
        dict: A dictionary with words as keys and their counts as values.

    Example:
        >>> count_words(['apple', 'banana', 'apple'])
        {'apple': 2, 'banana': 1}
    """
    counts = {}
    for word in word_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def print_counts(counts):
    """
    Print the word counts in a nicely formatted way.

    Args:
        counts (dict): Dictionary of word counts.
    """
    for word, count in counts.items():
        print(f"{word:10} {count}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
