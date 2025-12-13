import sys
from stats import count_words, char_frequency, sort_char_counts

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)      # word count
    chars = char_frequency(book_text)       # character count (lowercased, alphabetic only)

    sorted_chars = sort_char_counts(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item.get("char")
        num = item.get("num")
        if not ch or not ch.isalpha():
            continue
        print(f"{ch}: {num}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
