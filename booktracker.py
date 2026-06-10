# Book=[]
# print("Book Tracker")
# print("1. Add Book")
# print("2. Show Books")
# print("3. Delete books")
# print("4. Exit")
# while True:
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         new=input("Name of the book: ")
#         Book.append(new)
#         print("Book Added!")
#     elif choice == "2":
#         for book in Book:
#             print(book)
#     elif choice == "3":
#         delete=input("Which book do you want to delete?: ")
#         if delete in Book:
#             Book.remove(delete)
#             print("Book Deleted!")
#         else:
#             print("Book not Found.")
#     elif choice == "4":
#         break
#     else:
#         print("Invalid Choice.")

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

