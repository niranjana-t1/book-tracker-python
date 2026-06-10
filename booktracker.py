books=[]
def add():
    new=input("Name of the Book: ")
    books.append(new)
    print("Book Added!")
def show():
    if len(books)==0:
        print("No books found.")
    else:
        for book in books:
            print(book)
def delete():
    dlt=input("Which book do you want to delete?: ")
    if dlt in books:
        books.remove(dlt)
        print("Book deleted!")
    else:
        print("Book not found.")
 
while True:
    print("---BOOK TRACKER---\n")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Delete books")
    print("4. Exit")
    choice= input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        delete()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

