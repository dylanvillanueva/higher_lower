import random
import os
import art
import game_data


def generate_random_account():
    random_position = random.randint(0, len(game_data.data) - 1)
    random_account = game_data.data.pop(random_position)
    return random_account


play_game = True
score = 0
max_score = len(game_data.data)
print(max_score)
account1 = generate_random_account()

print(art.logo)

while play_game:
    print(len(game_data.data))
    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}.")

    print(art.vs)

    account2 = generate_random_account()
    print(f"Compare B: {account2['name']}, a {account2['description']}, from {account2['country']}.")

    if account1['follower_count'] > account2['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess == correct_answer:
        if correct_answer == 'b':
            account1 = account2
        score += 1
        # on windows
        os.system('cls')
        # on linux / os x
        # os.system('clear')
        if len(game_data.data) == 0:
            print(f"You win! Final score {score}")
            play_game = False
    else:
        # on windows
        os.system('cls')
        # on linux / os x
        # os.system('clear')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score {score}")
        play_game = False