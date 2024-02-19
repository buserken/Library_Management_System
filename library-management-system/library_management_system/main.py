class Library:
    def __init__(self):
        self.file = "books.txt"

    def __del__(self):
        if hasattr(self, 'file_handle'):
            self.file_handle.close()

    def open_file(self, mode):
        self.file_handle = open(self.file, mode)

    def list_books(self):
        with open(self.file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                book_info = line.strip().split(',')
                print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        with open(self.file, 'a') as file:
            file.write(f"{book_title},{book_author},{release_year},{num_pages}\n")
        print("Book added successfully.")

    def remove_book(self, title):
        with open(self.file, 'r') as file:
            lines = file.readlines()
        with open(self.file, 'w') as file:
            for line in lines:
                if not line.startswith(title):
                    file.write(line)
        print(f"Book '{title}' removed successfully.")


def main():
    lib = Library()
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            title = input("Enter the title of the book to remove: ")
            lib.remove_book(title)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
