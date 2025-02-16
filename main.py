def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = len(file_contents.split())

    character_stats = {}

    for c in file_contents:
        c_lower = c.lower() # c = character

        if c_lower.isalpha():
            if c_lower not in character_stats:
                character_stats[c_lower] = 1
            else:
                character_stats[c_lower] += 1

    new_character_stats = []

    for c in character_stats:
        v = character_stats[c]
        #print(character_stats)
        new_character_stats.append({"char":c, "val":v})

    def sort_by(dict):
        return dict["val"]

    rev_sorted_alpha = sorted(new_character_stats, reverse=True, key=sort_by)

    ## FINAL REPORT
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for c in rev_sorted_alpha:
        char = c["char"]
        val = c["val"]
        print(f"The '{char}' character was found {val} times")
    print("--- End report ---")
#def main():
#    with open("./books/frankenstein.txt") as f:
#        file_contents = f.read()
#        print(file_contents)
#    return file_contents
#
#count = 0
#
#def word_count():
#    count = len(main().split())
#
#def character_count(frank):
#    character_stats = {}
#    for w in frank:
#        w_lower = w.lower()
#
#        if w_lower not in character_stats:
#            character_stats[w_lower] = 1
#        else:
#            character_stats[w_lower] += 1
#    print(character_stats)
#    return character_stats
#
#def alpha_sort(char_stats):
#    new_alpha_chars = []
#    for s in char_stats:
#        v = char_stats[s]
#        if s.isalpha() == True:
#            new_alpha_chars.append({"char": s, "val": v})
#
#    # A function that takes a dictionary and returns the value of the "num" key
#    # This is how the `.sort()` method knows how to sort the list of dictionaries
#
#    def sort_by(dict):
#        return dict["val"]
#
#    for s in new_alpha_chars:
#        print(s["char"], s["val"])
#
#
#    new_alpha_chars_sorted = sorted(new_alpha_chars, key=sort_by, reverse=True)
#    #new_alpha_chars.sort(key=sort_by, reverse=True)
#    #print(new_alpha_chars)
#    #print(new_alpha_chars_sorted)
#    print("--- Begin report of books/frankenstein.txt ---")
#    print(f"{count} words found in the document")
#
#    print(new_alpha_chars_sorted)
#
#
main()
#word_count()
#character_count(main())
#alpha_sort(character_count(main()))
