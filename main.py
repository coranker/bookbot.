import sys

from stats import get_num_words, get_sorted_character

def main(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    for item in get_sorted_character(file_path):
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)