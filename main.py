from stats import word_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    word_count(file_contents)
main()
