from stats import get_num_character, get_num_words

def main(file_path):
    dict_characters = get_num_character(file_path)
    return print (f"Found {get_num_words(file_path)} total words", dict_characters)

main("books/frankenstein.txt")