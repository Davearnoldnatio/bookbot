""" The stats functions"""



def return_value(items):
    return items["num"]
    

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
        
def get_sorted_dict(character_count):
    list_of_dicts = []
    for word, value in character_count.items():
        if word.isalpha():
            list_of_dicts.append({"char" : word , "num" : value})
    list_of_dicts.sort(reverse=True, key = return_value)
    return list_of_dicts
    

