def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def word_count():
    word_count = main().split()
    print(len(word_count))

def character_count(frank):
    character_stats = {}
    for w in frank:
        w_lower = w.lower()

        if w_lower not in character_stats:
            character_stats[w_lower] = 1
        else:
            character_stats[w_lower] += 1
    print(character_stats)



main()
word_count()
character_count(main())
