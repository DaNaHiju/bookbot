from stats import count_words

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

# Execute the program
main()