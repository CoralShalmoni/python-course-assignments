from word_utils import count_words

def test_count_words_basic():
    words = ['apple', 'banana', 'apple']
    expected = {'apple': 2, 'banana': 1}
    assert count_words(words) == expected

def test_count_words_empty():
    assert count_words([]) == {}

def test_count_words_case_sensitive():
    words = ['Apple', 'apple', 'APPLE']
    expected = {'Apple': 1, 'apple': 1, 'APPLE': 1}
    assert count_words(words) == expected
