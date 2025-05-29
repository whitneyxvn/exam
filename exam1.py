def check_sentence(sentence):
    #Capital letter check
    if sentence[0].isupper():
        print("!Good start!")
    else:
        print("Your sentence should start with a capital letter.")

        #Full stop check
    if sentence.strip().endswith("."):
        print("Nice! You ended your sentence properly.")
    else:
        print("Don't forget to end your sentence with a full stop.")

    #Count commun conjuctions
    sentence_lower = sentence.lower()
    for word in ["and", "but", "because"]:
        count = sentence_lower.count(word)
        print(f"You used '{word}' {count} time(s).")

        #Word count
        words = sentence.split()
        print(f"Your sentence has {len(words)} word(s).")

        #Special character check
        no_spaces = sentence.replace(" ", "")
        if no_spaces.isalpha():
            print("Your sentence is clean. No strange characters.")
        else:
            print("Your sentence has some special characters. Clean it up!")

            #Centered success message
            print("Essay checked successfully".center(50))

#Number of times to check
max_checks = 0
sentence = input("Enter a sentence from your homework")
check_sentence(sentence)
if max_checks == 0:
 try_again = input("Doyou want to try again? (yes/no): ").strip().lower()
 if try_again != "yes":
    print("Thanks for using Essay Buddy. Happy writing!")
 if try_again == "yes":
    sentence = input("Enter a sentence from your homework")
    check_sentence(sentence)
    max_checks = 1
    


                
