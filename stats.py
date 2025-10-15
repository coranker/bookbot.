def get_book_text(file_path):
    """returns the contents of the file in a string"""
    with open(file_path) as file_contents:
        return file_contents.read()

def get_num_words(file_path):
    """returns a list of the text file with each word seperated by a space"""
    list_words = get_book_text(file_path).split()
    return len(list_words)

def get_num_character(file_path):
    lower_text_file = get_book_text(file_path).lower()
    list_text_file = list(lower_text_file)
    character_dict = {}
    for letter in list_text_file:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict