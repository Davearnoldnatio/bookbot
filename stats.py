def get_word_count(book_text):
    word_list = book_text.split()
    #gives a list of the words
    return len(word_list)

def get_character_count(book_text):
    lower_word_list = book_text.lower().strip()
    character_count = {}
    for word in lower_word_list:
        if word in character_count:
            character_count[word] += 1
        else:
            character_count[word] = 1
    return character_count
        
        
