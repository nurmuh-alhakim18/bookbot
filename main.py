def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_of_words = count_words(text)
  chars_count = count_chars(text)
  sorted_chars_tuple = sort_chars_count(chars_count)
  print(print_report(book_path, num_of_words, sorted_chars_tuple))

def get_book(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words  = text.split()
  return len(words)

def count_chars(text):
  chars_count = {}
  for char in text:
    if char.isalpha():
      lowered_char = char.lower()
      if lowered_char in chars_count:
        chars_count[lowered_char] += 1
      else:
        chars_count[lowered_char] = 1

  return chars_count

def sort_on(chars_count):
  return chars_count[1]

def sort_chars_count(chars_count):
  return sorted(chars_count.items(), reverse=True, key=sort_on)

def print_report(book_path, num_of_words, chars_tuple):
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_of_words} words found in the document\n\n")
  for k in chars_tuple:
    print(f"The '{k[0]}' character was found {k[1]} times")
  print("--- End report ---")

main()