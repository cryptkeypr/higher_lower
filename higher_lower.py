from art import logo, vs
from gamedata import data
import random

# compare A: person, profession, from where
# vs
# B
# who has more followers, a or b?
# right or wrong, current score:
score = 0
print(logo)
playing = True
while playing:
    choices = []
    for _ in range (2):
        choices.append(random.choice(data))

    if choices[0] == choices[1]:
        choices.remove([1])
        choices.append(random.choice(data))

    A = choices[0]['name']
    B = choices[1]['name']


    def pick_highest(choice1, choice2):
        if choice1 > choice2:
            return "A"
        else:
            return "B"


    answer = pick_highest(A, B)
    print(f"Psst.. the answer is {answer}")
    print(f"Compare A: {choices[0]['name']}, a {choices[0]['description']}, from {choices[0]['country']}")
    print(vs)
    print(f"Against B: {choices[1]['name']}, a {choices[1]['description']}, from {choices[1]['country']}")
    print("-'Q' to quit.")

    response = input("Who has more followers? Type 'A' or 'B': ").upper()
    if response == 'Q':
        playing = False
    elif response == answer:
        score += 1
        print(f"\nYou got it!  Current score: {score}")
    else:
        print(f"\nNo.. sorry, that is wrong.   Current score: {score}")
