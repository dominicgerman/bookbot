def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    char_count = number_of_chars(text)
    print_report(book_path, word_count, char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_chars(text):
    letters = {}
    book_str = text.lower()
    for letter in book_str:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def print_report(book_path, word_count, chars_dict):
    dicts = []
    for key, value in chars_dict.items():
        if key.isalpha():
             dicts.append({"char": key, "count": value})
    dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")
    for d in dicts:
        print(f"The '{d["char"]}' character was found {d["count"]} times")
    print(f"--- End of report ---")

main()
