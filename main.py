from stats import get_book_letters, get_book_words, sort_list


def main ():
    print("============ BOOKBOT ============")
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    book_contents = read_file (book_path)
    num_words = get_book_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_letters = get_book_letters(book_contents)
    sort_list(num_letters) 
    print("============= END ===============")
    
def read_file (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return (file_contents)
    
main ()
