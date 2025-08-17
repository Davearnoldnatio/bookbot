from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)   


def get_book_text(book):
    #function to return a book as a string
    #The book varaible here should be a filepath str
    with open (book) as f:
        return f.read()

def main():
    #main function
    book = sys.argv[1]


   

    book_text = get_book_text(book)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = get_sorted_dict(character_count)
    
    #word_count function taking get_book_text() as an argument
    print ('============ BOOKBOT ============')
    print ('Analyzing book found at books/frankenstein.txt...')
    print (f" Found {word_count} total words")
    print ("--------- Character Count -------")
    for event in sorted_character_count:
        print (f"{event["char"]}: {event["num"]}")
    print ("============= END ===============")
main()




    


