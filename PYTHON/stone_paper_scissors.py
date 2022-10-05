import random

print("\nWelcome to our Stone Paper Scissor Game\n")

# Take the input from the user
a = input("Enter a choice (stone, paper, scissors): ")

# Generate a random option for computer
b = random.choice(["stone", "paper", "scissors"])

print(f"\nYour Choice: {a}, Computer choice: {b}.\n")

print("Result:", end="")
if a == b:
    print(f"Both players selected {a}. It's a tie!")
elif a == "stone":
    if b == "scissors":
        print("Stone smashes scissors! You win!")
    else:
        print("Paper covers stone! You lose.")
elif a == "paper":
    if b == "stone":
        print("Paper covers stone! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif a == "scissors":
    if b == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Stone smashes scissors! You lose.")


print("\nThanks for playing!\n")
#updation
print("Hello")
print("Hello")
