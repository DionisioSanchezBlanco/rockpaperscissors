# Write your code here
import random

options_gamer = ["rock", "paper", "scissors"]
options_computer = ["rock", "paper", "scissors"]

# Check results. To improve in following stages with dictionary
def results(gamer, computer):
    if gamer == computer:
        print(f"There is a draw ({options_gamer[gamer]})")
    elif (gamer == 0 and computer == 2) or \
            (gamer == 1 and computer == 0) or \
            (gamer == 2 and computer == 1):
        print(f"Well done. The computer chose {options_computer[computer]} and failed")
    else:
        print(f"Sorry, but the computer chose {options_computer[computer]}")

# Random chose for Computer
cp_choice = random.choice(options_computer)

# Option from gamer
option = input()

# Get index to compare lists
ind_gamer = options_gamer.index(option)
ind_cpu = options_computer.index(cp_choice)

results(ind_gamer, ind_cpu)

#Another solution
'''
from random import choice

cpu=choice(['rock','paper','scissors'])
print(cpu)
player=input()

beats={'rock':'scissors','scissors':'paper','paper':'rock'}

if player==cpu:
  print(f"There is a draw ({cpu})")

elif beats[player]==cpu:
  print(f'Well done. Computer chose {cpu} and failed')

elif beats[cpu]==player:
  print(f'Sorry, but computer chose {cpu}')

'''
