# Initialize library with five books
library = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Moby Dick": "Herman Melville",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen"
}

# Normalize the title to be title case with correct spacing
def normalize_title(title):
    return ' '.join(title.strip().title().split())

# Add a book to the library with proper capitalization
def add_book(title, author):
    title_normalized = normalize_title(title)
    if title_normalized.lower() in (book.lower() for book in library.keys()):
        print("This book already exists in the library.")
    else:
        library[title_normalized] = author.strip().title()
        print("Book added successfully.")

# Remove a book from the library
def remove_book(title):
    title_normalized = normalize_title(title)
    found = False
    for key in library.keys():
        if key.lower() == title_normalized.lower():
            del library[key]
            print("Book removed successfully.")
            found = True
            break
    if not found:
        print("This book does not exist in the library.")

# Search for a book in the library
def search_book(title):
    title_normalized = normalize_title(title)
    found = False
    for key, author in library.items():
        if key.lower() == title_normalized.lower():
            print(f"The book '{key}' by '{author}' was found in the library.")
            found = True
            break
    if not found:
        print("Book not found.")

# List all books in alphabetical order
def list_books():
    sorted_books = sorted(library.items(), key=lambda x: x[0].lower())
    for book, author in sorted_books:
        print(f"{book} by {author}")

# Main function with the updated menu
def main():
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. List all books")
        print("5. Exit")

        choice = input("What would you like to do? Please enter a choice 1-5: ")

        if choice == '1':
            title = input("Please enter a book title: ")
            author = input("Please enter the author of the book: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Please enter the title of the book to remove: ")
            remove_book(title)

        elif choice == '3':
            title = input("Please enter the title of the book you would like to search for: ")
            search_book(title)

        elif choice == '4':
            list_books()

        elif choice == '5':
            print("End of the program.")
            break

        else:
            print("Please choose from the options provided.")

if __name__ == "__main__":
    main()
