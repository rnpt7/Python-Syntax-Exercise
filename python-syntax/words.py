def print_upper_words(words, must_start_with):
    """Print words starting with given letters in all uppercase.

    -words: list of words
    -must_start_with: letter(s) words must start with to be printed

    For example:

      print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
        
    should print:

      "HELLO", "HEY", "YO", "YES"
    """
    
    for word in words:
        if(word[0] in must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})