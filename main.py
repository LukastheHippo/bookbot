def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = word_count(book_text)
    counting_characters = character_count(book_text)
    sorted_list =character_sort(counting_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} in the book.")
    print()
    for entry in sorted_list:
        print(f"The character '{entry["char"]}' was found {entry["count"]} times")
    print(f"--- End report ---")

    character_sort(counting_characters)

def character_sort(char_count_dict):
    sorted_list = []
    for character in char_count_dict:
        sorted_list.append({"char": f"{character}", "count": char_count_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["count"]

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