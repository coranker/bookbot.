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
    for char in list_text_file:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def get_sorted_character(file_path):
    unsorted_char = get_num_character(file_path)
    sorted_list = []
    for char in unsorted_char:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = unsorted_char[char]
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list