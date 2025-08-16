""" The stats functions"""


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
        
def get_sorted_char_count(character_count):
    list_of_dict = []

    for key, value in character_count.items() and character_count.values().isalpha():
        list_of_dict.append({key: value})

    for character in list_of_dict:
        sorted_character_count = list_of_dict.sort(reverse=True, key = lambda a: list(a.items())[0][1])
    return sorted_character_count
