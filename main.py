book_path = "books/frankenstein.txt"

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    counter = {}
    content_lower = content.lower()
    for char in content_lower:
        if char.isalpha():
            if not char in counter:
                counter[char] = 1
            else:
                counter[char] += 1
    items = list(counter.items())
    items.sort(key=lambda tup: tup[0])
    return items

with open(book_path) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)

    print(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for item in letter_count:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")