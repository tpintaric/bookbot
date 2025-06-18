from stats import get_book_chars, get_book_words, report, sorted_book_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def get_book_text(path):
        with open(path) as f:
            book_text = f.read()

            #print(book_text)
            return book_text

    def main():
        #file_name = "./books/frankenstein.txt"
        file_name = sys.argv[1]
        entire_book = get_book_text(file_name)
        word_count = get_book_words(entire_book)
        book_char_stats = get_book_chars(entire_book)
        sorted_chars = sorted_book_chars(book_char_stats)
        report(word_count,sorted_chars, file_name)
    main()
    
