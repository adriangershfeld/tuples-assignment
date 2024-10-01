# Task 1: Library System Enhancement 
# Sharpen your skills in managing and modifying data within tuples and lists.
# You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, book):
    if book not in library:
        library.append(book)
    else:
        print(f"The book '{book}' is already in the library.")

new_book = ("The Hobbit", "J. R. R. Tolkien")
add_book(library, new_book)
print(library)

# Duplicate test
new_book = ("Brave New World", "Aldous Huxley")
add_book(library, new_book)
print(library)

