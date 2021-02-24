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
options = ['rock', 'paper', 'scissors']

name = input("Enter your name: ")
print(f"Hello, {name}")

if name not in score:
    score[name] = 0

player = input()

while player != "!exit":
    beats = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    cpu = choice(options)

    if player == "!rating":
        print(f"Your rating: {score[name]}")

    elif player not in options:
        print("Invalid input")

    elif player == cpu:
        print(f"There is a draw ({cpu})")
        score[name] += 50

    elif beats[player] == cpu:
        print(f'Well done. Computer chose {cpu} and failed')
        score[name] += 100

    elif beats[cpu] == player:
        print(f'Sorry, but computer chose {cpu}')

    player = input()

print("Bye!")
