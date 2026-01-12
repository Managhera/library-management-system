books = []#list

def add_book():
    #title can capital first letter of word
    #strip used remove extaa space
    acc = input("Accession Number: ").strip()
    isbn = input("ISBN: ").strip()
    title = input("Book Title: ").strip().title()
    author = input("Author Name: ").strip().title()
    publisher = input("Publisher: ").strip().title()
    year = input("Year of Publication: ").strip()
    category = input("Category: ").strip().title()
    copies_total = int(input("Total Copies: "))
    
    book = {#dict
        "acc": acc,
        "isbn": isbn,
        "title": title,
        "author": author,
        "publisher": publisher,
        "year": year,
        "category": category,
        "copies": copies_total,
        "available": copies_total
    }
    
    books.append(book)
    print(f"\n Book '{title}' added successfully!\n")

# Display All Books
def display_books():
    if not books:
        print("No books in library.\n")
        return
    
    print("\n======= ALL BOOKS =======")
    for i, book in enumerate(books, start=1):
        print(f"\nBook No       : {i}")
        print(f"Accession No  : {book['acc']}")
        print(f"ISBN          : {book['isbn']}")
        print(f"Title         : {book['title']}")
        print(f"Author        : {book['author']}")
        print(f"Publisher     : {book['publisher']}")
        print(f"Year          : {book['year']}")
        print(f"Category      : {book['category']}")
        print(f"Total Copies  : {book['copies']}")
        print(f"Available     : {book['available']}")

#Update Book
def update_book():
    display_books()
    index = int(input("Enter Book No to update: ")) 
    if 0 <= index < len(books):
        book = books[index]

        while True:
            print("""Which field do you want to update?\n1. Title\n2. Author\n3. Publisher\n4. Year\n5. Category\n6. Total Copies\n0. Finish updating""")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                book["title"] = input("New Title: ").strip().title()
            elif choice == "2":
                book["author"] = input("New Author: ").strip().title()
            elif choice == "3":
                book["publisher"] = input("New Publisher: ").strip().title()
            elif choice == "4":
                book["year"] = input("New Year: ").strip()
            elif choice == "5":
                book["category"] = input("New Category: ").strip().title()
            elif choice == "6":
                book["copies"] = int(input("New Total Copies: "))
                book["available"] = book["copies"]
            elif choice == "0":
                break
            else:
                print("Invalid choice, try again.")

        print("Book updated successfully.\n")
    else:
        print("Invalid Book No.\n")


#Delete Book 
def delete_book():
    display_books()
    index = int(input("Enter Book No to delete: ")) - 1
    if 0 <= index < len(books):
        removed = books.pop(index)
        print(f"Book '{removed['title']}' deleted successfully.\n")
    else:
        print("Invalid Book No.\n")



# --- Main Menu ---
def main_menu():
    while True:
        print("0 : Exit\n1 : Add Book\n2 : Display All Books\n3 : Update Book\n4 : Delete Book")
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        elif choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        else:
            print("Invalid choice.\n")

main_menu()
