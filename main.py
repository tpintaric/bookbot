from stats import get_book_chars, get_book_words

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        #print(book_text)
        return book_text
   
def main():
    entire_book = get_book_text("./books/frankenstein.txt")
    get_book_words(entire_book)
    get_book_chars(entire_book)
    
main()
    
