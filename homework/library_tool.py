# Simple Library Borrowing System

borrow_history = []

# Days of the week in order to simulate "overdue" logic
week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def borrow_book():
    student_name = input("Student name: ").strip().title()
    book_title = input("Book title: ").strip().title()
    borrow_day = input("Borrowed on (e.g. Monday): ").strip().lower()
    return_day = input("Return by (e.g. Friday): ").strip().lower()

    record = {
        "student": student_name,
        "book": book_title,
        "borrow_day": borrow_day,
        "return_day": return_day
    }

    borrow_history.append(record)
    print("\n✔️ Book recorded successfully!\n")

def view_history():
    if not borrow_history:
        print("No borrowing history found. Please record a borrowed book first.\n")
        return

    print("\n📘 Borrowing History:")
    today = input("Enter today's day (e.g. Wednesday): ").strip().lower()

    for record in borrow_history:
        student = record["student"]
        book = record["book"]
        borrow_day = record["borrow_day"].capitalize()
        return_day = record["return_day"].capitalize()
        sentence = f"{student} borrowed '{book}' on {borrow_day}, expected to return by {return_day}."
        print(sentence)

        # Overdue check using index in week_days
        try:
            today_index = week_days.index(today)
            return_index = week_days.index(record["return_day"])
            if today_index > return_index:
                print("⚠️ The book is overdue! Please remind the student.\n")
        except ValueError:
            print("⚠️ Could not determine if overdue – invalid day input.\n")

def main():
    while True:
        print("What would you like to do?")
        print("1. Borrow a book")
        print("2. View borrowing history")
        print("3. Exit")
        choice = input("→ ").strip()

        if choice == "1":
            borrow_book()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")

# Run the program
main()
