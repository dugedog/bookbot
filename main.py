from stats import get_book_letters, get_book_words, sort_list
import sys

def main ():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
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
