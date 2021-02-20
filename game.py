# Write your code here
options_computer = ["rock", "paper", "scissors"]
option = input()

if option == "rock":
    print(f"Sorry, but the computer chose {options_computer[1]}")
elif option == "paper":
    print(f"Sorry, but the computer chose {options_computer[2]}")
else:
    print(f"Sorry, but the computer chose {options_computer[0]}")
