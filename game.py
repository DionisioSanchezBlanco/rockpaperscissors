from random import choice, seed

# Another way to get the dictionary score
# rating = [line.split() for line in open("rating.txt", "r").readlines()]
# rating = {name: int(score) for name, score in rating}

# Read the file with scores and create the dictionary {name:score}
def score_values():
    file_ = open("rating.txt", 'r')
    score = []
    for line in file_:
        list_line = line.split()
        score.extend(list_line)

    score_dict = {score[i]: int(score[i+1]) for i in range(0, len(score), 2)}
    file_.close()
    return score_dict

score = score_values()

# Dictionary with all winning cases
beats = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
default_options = ['rock', 'paper', 'scissors']

name = input("Enter your name: ")
print(f"Hello, {name}")

if name not in score:
    score[name] = 0

options = input().split(',')

if options == ['']:
    options = default_options
print("Okay, let's start")

player = input()

while player != "!exit":
    cpu = choice(options)
    if player == "!rating":
        print(f"Your rating: {score[name]}")

    elif player not in options:
        print("Invalid input")

    elif player == cpu:
        print(f"There is a draw ({cpu})")
        score[name] += 50

    elif cpu in beats[player]:
        print(f'Well done. Computer chose {cpu} and failed')
        score[name] += 100

    elif player in beats[cpu]:
        print(f'Sorry, but computer chose {cpu}')

    player = input()

print("Bye!")
