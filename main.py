from stats import get_num_words
from stats import count_characters
from stats import sort_characters
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = count_characters(text)
    sorted_chars = sort_characters(num_char)

    

    

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
            
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()