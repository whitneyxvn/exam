# 🌟 Digital Yearbook Page Builder 🌟

# Step 1: Ask for Inputs
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
favourite_subject = input("Enter your favourite subject: ")
quote = input("Enter a quote or school memory: ")
hobbies = input("Enter at least one hobby (you can list more, separated by commas): ")
graduation_year = input("Enter your graduation year (e.g., 2026): ")

# Step 2: Process Inputs
# Format name with .title() and append "Sonuyi"
full_name = first_name.title() + " Sonuyi"

# Make the quote uppercase and replace "school" with "TECH SCHOOL"
formatted_quote = quote.upper().replace("SCHOOL", "TECH SCHOOL")

# Count the number of characters in the original quote
quote_length = len(quote)

# Center the title
yearbook_title = f"🌟 {graduation_year} GRADUATION YEARBOOK 🌟".center(50)

# Assign a badge based on subject
subject = favourite_subject.strip().lower()
if subject == "science":
    badge = "🧠 SMART THINKER"
elif subject == "math":
    badge = "🧮 NUMBER WIZARD"
elif subject == "art":
    badge = "🎨 CREATIVE MIND"
elif subject == "english":
    badge = "✍️ WORD MASTER"
elif subject in ["ict", "coding", "ict / coding"]:
    badge = "💻 CODE CHAMPION"
else:
    badge = "🏅 FUTURE STAR"

# Step 3: Display Output
print("\n" + "-" * 50)
print(yearbook_title)
print("-" * 50)
print()
print(f"Name        : {full_name}")
print(f"Age         : {age}")
print(f"Subject Tag : {favourite_subject.title()}")
print(f"Quote       : \"{formatted_quote}\"")
print(f"Hobbies     : {hobbies}")
print(f"Badge       : {badge}")
print()
print("Your digital yearbook profile has been created!")

# Optional: Show character count (optional feature)
print(f"(Your quote has {quote_length} characters.)")
