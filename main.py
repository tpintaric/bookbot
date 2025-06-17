def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        #print(book_text)
        return book_text

def get_book_words(entire_book):
    num_words = len(entire_book.split())
    print(f"{num_words} words found in the document")
   
def main():
    entire_book = get_book_text("./books/frankenstein.txt")
    get_book_words(entire_book)
    
main()
    
