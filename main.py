def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = word_count(book_text)
    print(f"There are {num_words} in the book.")
    counting_characters = character_count(book_text)
    print(f"Count of each character in book: {counting_characters}")

def character_count(book_text):
    all_lowercase = book_text.lower() # convert string to lowercase
    set_of_characters = set(all_lowercase) # remove duplicates
    count_of_characters = {}
    # set character values to 0 in order to update in place.
    for character in set_of_characters:
        count_of_characters[character] = 0
    # count all characters into dictionary
    for character in all_lowercase:
        count_of_characters[character] += 1
    
    return count_of_characters
        

def word_count(book_text):
    count = 0
    words = book_text.split()
    for word in words:
        count += 1
    return count

def open_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()