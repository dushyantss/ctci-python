"""
Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
"""


def word_frequencies(book, word):
    count = 0
    word_lower = word.lower()
    for w in book:
        if w.lower() == word_lower:
            count += 1
    return count


def multi_word_frequencies(book):
    cache = {}
    for w in book:
        lower_word = w.lower()
        cache[lower_word] = cache.get(lower_word, 0) + 1

    def find_word_in_book(word):
        return cache.get(word.lower(), 0)

    return find_word_in_book


if __name__ == "__main__":
    book = ["al", "go", "rithm", "go"]
    print(word_frequencies(book, "go"))
    print(word_frequencies(book, "a"))
    print(word_frequencies(book, "al"))
    cache = multi_word_frequencies(book)
    print(cache("a"))
    print(cache("al"))
    print(cache("go"))
