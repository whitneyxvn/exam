import json
import random
import string
import os

# 🔐 Generate a 6-character membership code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# 📁 Load member data from JSON file
def load_members():
    if os.path.exists("members.json"):
        with open("members.json", "r") as file:
            return json.load(file)
    return {}

# 💾 Save member data to JSON file
def save_members(members):
    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)

# 🧍 Register a new member
def register_member():
    print("\n📝 Register a New Member")
    name = input("Full Name: ").title()
    student_class = input("Class (e.g., Year 9): ").title()
    fav_subject = input("Favourite Subject: ").title()
    email = input("Email: ")

    code = generate_code()
    members = load_members()

    members[code] = {
        "name": name,
        "class": student_class,
        "favourite_subject": fav_subject,
        "email": email
    }

    save_members(members)

    print(f"\n✅ Registration successful, {name}!")
    print(f"📚 Your membership code is: {code}")
    print("Keep it safe to view your membership info.\n")

# 🔍 View member information using their code
def view_member():
    print("\n🔎 View Member Info")
    code = input("Enter your membership code: ").strip().upper()
    members = load_members()

    if code in members:
        member = members[code]
        print("\n✅ Member Found!")
        print(f"Name             : {member['name']}")
        print(f"Class            : {member['class']}")
        print(f"Favourite Subject: {member['favourite_subject']}")
        print(f"Email            : {member['email']}\n")
    else:
        print("❌ Sorry, no member found with that code.\n")

# 🚪 Exit message
def exit_program():
    print("\nGoodbye! 📘📗📕\n")

# 🚀 Main program
def main():
    print("📚 Welcome to the School Library Membership System")

    while True:
        print("\nWhat would you like to do?")
        print("1. Register a new member")
        print("2. View a member using their code")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            register_member()
        elif choice == "2":
            view_member()
        elif choice == "3":
            exit_program()
            break
        else:
            print("❗ Invalid choice. Please enter 1, 2, or 3.")

# ✅ Run the program
if __name__ == "__main__":
    main()

   
