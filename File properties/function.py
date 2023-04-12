
import csv

# Step 1: Read file and return list of dictionaries
def read_books(file_name):
    books = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Step 2: Get list of books by author name
def get_books_by_author(author_name, books):
    author_books = []
    for book in books:
        if book['author'] == author_name:
            author_books.append(book)
    return author_books

# Step 3: Get book details by ISBN number
def get_book_by_isbn(isbn_number, books):
    for book in books:
        if book['ISBN'] == isbn_number:
            return f"Title: {book['title']}, Price: {book['price']}"
    return 'Book not found'

# Step 4: Get list of books by price range
def get_books_by_price(min_price, max_price, books):
    price_range_books = []
    for book in books:
        if min_price <= float(book['price']) <= max_price:
            price_range_books.append(book)
    return price_range_books

# Step 5: Add new book to file
def add_new_book(file_name, new_book):
    with open(file_name, mode='a', newline='') as file:
        fieldnames = ['title', 'author', 'ISBN', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_book)

# User Interface
def main():
    file_name = 'books.csv'
    books = read_books(file_name)
    print('Welcome to the Bookstore\n')
    while True:
        print('Choose an option:')
        print('1. Search books by author')
        print('2. Search book by ISBN')
        print('3. Search books by price range')
        print('4. Add new book')
        print('5. Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            author_name = input('Enter author name: ')
            author_books = get_books_by_author(author_name, books)
            if author_books:
                for book in author_books:
                    print(f"Title: {book['title']}, Price: {book['price']}")
            else:
                print('No books found for the author')
        elif choice == '2':
            isbn_number = input('Enter ISBN number: ')
            book_details = get_book_by_isbn(isbn_number, books)
            print(book_details)
        elif choice == '3':
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            price_range_books = get_books_by_price(min_price, max_price, books)
            if price_range_books:
                for book in price_range_books:
                    print(f"Title: {book['title']}, Price: {book['price']}")
            else:
                print('No books found within the price range')
        elif choice == '4':
            new_book = {}
            new_book['title'] = input('Enter book title: ')
            new_book['author'] = input('Enter book author: ')
            new_book['ISBN'] = input('Enter book ISBN: ')
            new_book['price'] = input('Enter book price: ')
            add_new_book(file_name, new_book)
            print('Book added successfully')
        elif choice == '5':
            print('Thank you for visiting the Bookstore')
            break
        else:
            print('Invalid choice. Please choose again')

if __name__ == '__main__':
    main()



