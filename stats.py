def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return print(file_contents)

def get_book_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = file_contents.split()
    return print(f"{len(num_words)} words found in the document")


def get_book_letters(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    count = {}

    for letter in file_contents:
        if count.get(letter,"Invalid") == "Invalid":
            count.update({letter : 1})
        else:
            increment = count.get(letter) 
            increment += 1
            count.update({letter : increment}) 
            
    return print (count)


