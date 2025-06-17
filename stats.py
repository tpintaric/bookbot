def get_book_words(entire_book):
    num_words = len(entire_book.split())
    print(f"{num_words} words found in the document")

def get_book_chars(entire_book):
    book_chars = {}
    for c in entire_book:
        lower_c = c.lower()
        if lower_c not in book_chars:
            book_chars[lower_c] = 1
        else:
            book_chars[lower_c] +=1
    print(book_chars)
