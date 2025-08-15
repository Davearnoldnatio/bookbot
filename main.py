
def get_book_text(book):
    #function to return a book as a string
    #The book varaible here should be a filepath str
    with open (book) as f:
        return f.read()

def get_word_count(book_text):
    word_list = book_text.split()
    #gives a list of the words
    return len(word_list)

def main():
    #main function
    book = "books/frankenstein.txt"

    book_text = get_book_text(book)
    word_count = get_word_count(book_text)
    #word_count function taking get_book_text() as an argument
    print(f"{word_count} words found in the document")
    
main()




    


