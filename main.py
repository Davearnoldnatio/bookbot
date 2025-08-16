
def get_book_text(book):
    #function to return a book as a string
    #The book varaible here should be a filepath str
    with open (book) as f:
        return f.read()

def main():
    #main function
    book = "books/frankenstein.txt"

    from stats import get_word_count
    from stats import get_character_count
    from stats import get_sorted_char_count

    book_text = get_book_text(book)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = get_sorted_char_count(character_count)
    #word_count function taking get_book_text() as an argument
    print(f"{word_count} words found in the document")
    print(character_count)
    print(sorted_character_count)

main()




    


