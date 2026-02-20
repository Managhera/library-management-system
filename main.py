books = []#list
members = []        # List of member dictionaries
issued_books = set()  # Set of issued book accession numbers
transactions = []  

roles = {
    "admin": {"password": "admin123"}
}

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


#Search Function 
def search_books():
    if not books:
        print("No books in library.\n")
        return

    print("""
Search Book By:
1. Title
2. Author
3. Accession Number
4. ISBN
5. Publisher
6. Category
""")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        key = input("Enter Title: ").strip().lower()
    elif choice == "2":
        key = input("Enter Author Name: ").strip().lower()
    elif choice == "3":
        key = input("Enter Accession Number: ").strip().lower()
    elif choice == "4":
        key = input("Enter ISBN: ").strip().lower()
    elif choice == "5":
        key = input("Enter Publisher Name: ").strip().lower()
    elif choice == "6":
        key = input("Enter Category: ").strip().strip().lower()
    else:
        print("Invalid choice.\n")
        return

    found = False

    for book in books:
        if (
            (choice == "1" and key in book["title"].lower()) or
            (choice == "2" and key in book["author"].lower()) or
            (choice == "3" and key == book["acc"].lower()) or
            (choice == "4" and key == book["isbn"].lower()) or
            (choice == "5" and key in book["publisher"].lower()) or
            (choice == "6" and key in book["category"].lower())
        ):
            print("\n--- Book Found ---")
            print("Title     :", book["title"])
            print("Author    :", book["author"])
            print("Acc No    :", book["acc"])
            print("ISBN      :", book["isbn"])
            print("Category  :", book["category"])
            print("Available :", book["available"])
            found = True

    if not found:
        print("No book found.\n")



#Member Functions
def add_member():
    name = input("Member Name: ").strip().title()
    member_id = input("Member ID: ").strip()

    # Prevent duplicate member ID
    if any(m['id'] == member_id for m in members):
        print("Member ID already exists.\n")
        return

    member = {"name": name, "id": member_id}
    members.append(member)
    print(f"Member '{name}' added successfully!\n")

def issue_book_member(member_id):
    display_books()
    acc = input("Enter Accession Number: ").strip()

    book = next((b for b in books if b["acc"] == acc), None)
    if not book:
        print("Book not found.\n")
        return
    if book["available"] <= 0:
        print("Book not available.\n")
        return

    book["available"] -= 1
    issued_books.add(acc)
    transactions.append({"action": "issue", "acc": acc, "member_id": member_id})
    print(f"Book '{book['title']}' issued successfully!\n")



def return_book_member(member_id):
    acc = input("Enter Accession Number to return: ").strip()
    if acc in issued_books:
        book = next((b for b in books if b["acc"] == acc), None)
        if book:
            book["available"] += 1
            issued_books.remove(acc)
            transactions.append({"action": "return", "acc": acc, "member_id": member_id})
            print(f"Book '{book['title']}' returned successfully.\n")
    else:
        print("This book is not issued.\n")




def admin_menu():
    while True:
        print("""
Admin Menu:
1 : Add Book
2 : Display All Books
3 : Update Book
4 : Delete Book
5 : Search Books
6 : Add Member
0 : Logout
""")
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
        elif choice == '5':
            search_books()
        elif choice == '6':
            add_member()
        else:
            print("Invalid choice.\n")

def member_menu(member_id):
    while True:
        print(f"""
Member Menu (ID: {member_id}):
1 : Search Books
2 : Issue Book
3 : Return Book
0 : Logout
""")
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        elif choice == '1':
            search_books()
        elif choice == '2':
            issue_book_member(member_id)
        elif choice == '3':
            return_book_member(member_id)
        else:
            print("Invalid choice.\n")



# --- Main Menu ---
def login():
    while True:
        print("Library Management System")
        role = input("Login as (admin/member/exit): ").strip().lower()
        if role == "exit":
            break
        elif role == "admin":
            password = input("Enter admin password: ").strip()
            if password == roles["admin"]["password"]:
                admin_menu()
            else:
                print("Wrong password.\n")
        elif role == "member":
            member_id = input("Enter your Member ID: ").strip()
            if any(m["id"] == member_id for m in members):
                member_menu(member_id)
            else:
                print("Member not found. Contact admin.\n")
        else:
            print("Invalid role.\n")


login()