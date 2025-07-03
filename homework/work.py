# Mood Tracker App

# 1. 👋 Welcome the User
print("🌟 Welcome to Your Daily Mood Tracker 🌟\n")

name = input("What’s your name? ").title()
print(f"\nHi {name}, it’s great to see you! Let’s check in. 💬")

# 2. 🌤️ Ask for Mood
mood = input("\nHow are you feeling today? (happy, okay, tired, anxious, angry, etc.): ").lower()

if mood == "happy":
    print("That’s awesome! Keep smiling 😊")
elif mood == "tired":
    print("Rest is important. Don’t forget to breathe.")
elif mood == "anxious":
    print("Take things one step at a time. You’re doing fine.")
elif mood == "okay":
    print("Glad to hear it. Stay balanced.")
else:
    print("Thanks for sharing. You’re not alone.")

# 3. 🧮 Rate the Day
while True:
    try:
        rating = int(input("\nRate your day from 1 to 10: "))
        if 1 <= rating <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Please enter a valid number.")

if rating >= 8:
    print("Sounds like a great day!")
elif 5 <= rating < 8:
    print("Not bad, could be better. Keep going.")
else:
    print("Tough days happen. Tomorrow is a new chance.")

# 4. 🙏 Gratitude Prompt
gratitude = input("\nWhat’s one thing you’re grateful for today? ")
print(f"That’s wonderful. Being grateful for '{gratitude.capitalize()}' is powerful.")

# 5. 📋 Summary Report
print("\n" + "📋".center(40, "-"))
print(f"🌟 Mood Report for {name} 🌟".center(40))
print("-" * 40)
print(f"- Mood: {mood.capitalize()}")
print(f"- Day Rating: {rating}/10")
print(f"- Gratitude: {gratitude.capitalize()}")
print("-" * 40)
print("See you again tomorrow! 👋".center(40))
print("-" * 40)
