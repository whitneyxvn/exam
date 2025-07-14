import json
import random
import string
import os

# 🔐 Function to generate a 6-character access code
def generate_access_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# 📁 Function to load existing codes from the JSON file
def load_codes():
    if os.path.exists("codes.json"):
        with open("codes.json", "r") as file:
            return json.load(file)
    return {}

# 💾 Function to save updated codes back to the JSON file
def save_codes(codes):
    with open("codes.json", "w") as file:
        json.dump(codes, file, indent=4)

# ✍️ Register a new student
def register_student():
    print("🎓 Welcome to the Tech Seminar Registration!")
    
    name = input("Full Name: ").title()
    age = input("Age: ")
    school = input("School Name: ").title()
    email = input("Email Address: ")

    access_code = generate_access_code()
    codes = load_codes()

    codes[access_code] = {
        "name": name,
        "age": age,
        "school": school,
        "email": email
    }

    save_codes(codes)

    print(f"\n✅ Registration successful, {name}!")
    print(f"🎟️ Your access code is: {access_code}")
    print("Keep it safe — you’ll need it to attend the seminar.\n")

# 🧾 Verify an access code
def verify_code():
    codes = load_codes()
    user_code = input("Enter your access code to verify: ").strip().upper()

    if user_code in codes:
        student = codes[user_code]
        print("\n✅ Code found! Here's your registration info:")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"School : {student['school']}")
        print(f"Email  : {student['email']}\n")
    else:
        print("❌ Sorry, that access code is not registered.\n")

# 🚀 Main Program
def main():
    print("=== Tech Seminar Access System ===")
    print("1. Register a new student")
    print("2. Verify access code")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        register_student()
    elif choice == "2":
        verify_code()
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()