word_per_page = 0
pages=0
try:
    pages = int(input("Number of pages: "))
except ValueError:
    print("Please enter a valid input")
word_per_page =int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
