
def get_book_words(entire_book):
    num_words = len(entire_book.split())
    #print(f"{num_words} words found in the document")
    return num_words

def get_book_chars(entire_book):
    book_char_stats = {}
    for c in entire_book:
        lower_c = c.lower()
        if lower_c not in book_char_stats:
            book_char_stats[lower_c] = 1
        else:
            book_char_stats[lower_c] +=1
    return book_char_stats

def sorted_book_chars(book_char_stats):
    book_chars_alpha = []

    for ch in book_char_stats:
        key = ch
        val = book_char_stats[ch]

        if ch.isalpha() == True:
            book_chars_alpha.append({"char":key, "num":val} )

    def sort_by(dict):
        return dict["num"]

    sorted_chars_alpha = sorted(book_chars_alpha, reverse=True, key=sort_by)
    # Alternative way of writing would be:
    # book_chars_alpha.sort(reverse=True, key=sort_by)
    #print(book_chars_alpha)

    #print(sorted_chars_alpha)
    #print(book_chars_alpha) 
    
    return sorted_chars_alpha

def report(word_count, sorted_chars, file_name):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for s in sorted_chars:
        print(f"{s["char"]}: {s["num"]}")
        # {"char":key, "num":val}
        #print(f"{s["char"]}: {s["num"]}")
    
    print("============= END ===============")
