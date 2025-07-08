import random

# Version info
print("🔢 SmartCalc v1.0\n")

# Welcome screen
name = input("What's your name? ")
print(f"Welcome to SmartCalc, built by {name}!\n")

# Function to validate numeric input
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ That doesn't look like a number. Please try again.")

# Function for surprise mode
def surprise_me():
    surprises = [
        lambda: print("😂 Joke: Why did the math book look sad? Because it had too many problems!"),
        lambda: print("🧠 Riddle: I am a three-digit number. My tens digit is five more than my ones digit. My hundreds digit is eight less than my tens digit. What number am I? (Answer: 194)"),
        lambda: guess_the_number,
        lambda: print("🥚 You just discovered an Easter Egg!")
    ]
    chosen = random.choice(surprises)
    if chosen == guess_the_number:
        chosen()
    else:
        chosen()

# Mini-game for surprise mode
def guess_the_number():
    secret = random.randint(1, 10)
    guess = input("🎯 I'm thinking of a number between 1 and 10. Take a guess: ")
    try:
        guess = int(guess)
        if guess == secret:
            print("🎉 Whoa! You guessed it!")
        else:
            print(f"😅 Nope! I was thinking of {secret}.")
    except ValueError:
        print("🚫 That wasn't a number!")

# Main loop
while True:
    print("\nWhich operation would you like to perform?")
    print("(a) Add\n(b) Subtract\n(c) Multiply\n(d) Divide\n(e) Surprise Me!")

    choice = input("Enter your choice: ").lower()

    if choice in ['a', 'b', 'c', 'd']:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == 'a':
            result = num1 + num2
            print(f"🧮 The result of {num1} + {num2} is {result}")
        elif choice == 'b':
            result = num1 - num2
            print(f"🧮 The result of {num1} - {num2} is {result}")
        elif choice == 'c':
            result = num1 * num2
            print(f"🧮 The result of {num1} * {num2} is {result}")
        elif choice == 'd':
            if num2 == 0:
                print("🚫 Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"🧮 The result of {num1} / {num2} is {result}")
    elif choice == 'e':
        surprise_me()
    else:
        print("❗ Invalid choice. Please select a valid option.")

    again = input("\nWould you like to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("🙏 Thanks for using SmartCalc! See you next time.")
        break
