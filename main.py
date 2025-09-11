from stats import get_book_letters
from stats import get_book_words


def main ():

    get_book_words("/home/drexes/workspace/github.com/dugedog/bookbot/books/frankenstein.txt")
    num_letters = get_book_letters("/home/drexes/workspace/github.com/dugedog/bookbot/books/frankenstein.txt")
    print (num_letters)
    
main ()
