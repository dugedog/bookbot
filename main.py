from stats import get_book_letters, get_book_words


def main ():
    book_path = "books/frankenstein.txt"
    book_contents = read_file (book_path)
    num_words = get_book_words(book_contents)
    num_letters = get_book_letters(book_contents)
    print(f"{num_words} found in document")
    print(num_letters)
    
    
    
def read_file (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return (file_contents)
    
main ()
