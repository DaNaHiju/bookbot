#function that accepts the text from the book and counts the number of words in it
def count_words(text):
    words = text.split()
    return len(words)
