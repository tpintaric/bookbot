def word_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        print(len(word_count))

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


main()
word_count()
