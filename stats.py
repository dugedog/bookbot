def get_book_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words


def get_book_letters(file_contents):
    file_contents = file_contents.lower()
    count = {}
    for letter in file_contents:
        if count.get(letter,"Invalid") == "Invalid":
            count.update({letter : 1})
        else:
            count[letter] +=1        
    return count

def sort_list(unsorted_list):
    sorted_list = []
    for pair in unsorted_list:
        if pair.isalpha()==False:
            continue
        sorted_list.append({"char":pair, "num": unsorted_list.get(pair)})
        sorted_list.sort(reverse=True, key="num")
    return(sorted_list)
   
