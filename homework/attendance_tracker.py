# Simple Attendance Tracker

attendance_data = {}

def take_attendance():
    num_students = int(input("How many students today? → "))
    for _ in range(num_students):
        name = input("Enter name: ").title()
        while True:
            status = input(f"Was {name} present or absent? → ").strip().lower()
            if status in ["present", "absent"]:
                attendance_data[name] = status
                break
            else:
                print("Please enter 'present' or 'absent' only.")
    print("\nAttendance saved!\n")

def view_remarks():
    if not attendance_data:
        print("No attendance data available. Please take attendance first.\n")
        return
    print("\n📋 Attendance Remarks:")
    for name, status in attendance_data.items():
        if status == "present":
            remark = "✅ Present – Keep it up!"
        else:
            remark = "❌ Absent – Please catch up on missed lessons."
        print(f"{name} - {remark}")
    print()

def main():
    while True:
        print("What would you like to do?")
        print("1. Take attendance")
        print("2. View attendance remarks")
        print("3. Exit")
        choice = input("→ ").strip()

        if choice == "1":
            take_attendance()
        elif choice == "2":
            view_remarks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Run the program
main()
