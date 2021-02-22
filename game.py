from random import choice, seed

options = ['rock', 'paper', 'scissors']

player = input()

while player != "!exit":
  beats = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}

  cpu = choice(options)
  
  if player not in options:
    print("Invalid input")

  elif player == cpu:
    print(f"There is a draw ({cpu})")

  elif beats[player] == cpu:
    print(f'Well done. Computer chose {cpu} and failed')

  elif beats[cpu] == player:
    print(f'Sorry, but computer chose {cpu}')

  player = input()

print("Bye!")
