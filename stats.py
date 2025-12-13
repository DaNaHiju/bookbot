#function that accepts the text from the book and counts the number of words in it
def count_words(text):
    words = text.split()
    return len(words)

# Function accepts the text from the book as a string and returns the number of times
# each lowercase alphabetic character appears in the string.
def char_frequency(text):
    """
    Return a dictionary mapping each lowercase alphabetic character to its frequency.

    The function converts `text` to lowercase with `lower()` to avoid counting
    uppercase and lowercase separately, and counts only alphabetic characters
    (so the result will be keys like `'a'`, `'b'`, ...).
    """
    freq = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def sort_char_counts(freq_dict):
    """
    Convert a dictionary of character->count into a list of dictionaries
    of the form {"char": <char>, "num": <count>} sorted from greatest
    to least by the "num" value.

    Uses the list.sort() method and a helper function for the sort key.
    """
    items = [{"char": k, "num": v} for k, v in freq_dict.items()]

    def _num_key(d):
        return d.get("num", 0)

    items.sort(key=_num_key, reverse=True)
    return items

