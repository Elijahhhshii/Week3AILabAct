def check_borrowing(overdue_books, status):
    if overdue_books == "yes":
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


allowed_students = 0

while True:
    print("\n= Library Kiosk =")

    name = input("Enter student name (or 'exit' to quit): ").strip()

    if name.lower() == "exit":
        break

    overdue_books = input("Do you have overdue books? (yes/no): ").strip().lower()
    status = input("Enter borrower status (active/suspended): ").strip().lower()

    try:
        books = int(input("How many books do you want to borrow? "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    result = check_borrowing(overdue_books, status)

    if result == "Borrowing allowed":
        if books <= 0:
            print("Error: You must borrow at least 1 book.")
        elif books > 3:
            print("Warning: You can only borrow up to 3 books.")
            print("Borrowing approved for 3 books.")
            allowed_students += 1
        else:
            print(f"Borrowing approved for {books} book(s).")
            allowed_students += 1
    else:
        print(result)

print("\nLibrary session ended.")
print("Total students allowed to borrow books:", allowed_students)
