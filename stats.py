def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return print(file_contents)

def get_book_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = file_contents.split()
    return print(f"{len(num_words)} words found in the document")
