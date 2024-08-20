import art
import game_data as gd
import random

game = True
current_score = 0
final_score = 0
first_number = random.randint(0, len(gd.data) - 1)

print(art.logo)

while game:

    second_number = random.randint(0, len(gd.data) - 1)
    while second_number == first_number:
        second_number = random.randint(0, len(gd.data) - 1)

    first_data_chosen = gd.data[first_number]
    second_data_chosen = gd.data[second_number]

    first_followers = first_data_chosen['follower_count']
    second_followers = second_data_chosen['follower_count']

    print(f"{first_data_chosen['name']}, {first_data_chosen['description']}, from {first_data_chosen['country']}")
    print(art.vs)
    print(f"{second_data_chosen['name']}, {second_data_chosen['description']}, from {second_data_chosen['country']}\n")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == "A" and first_followers > second_followers:
        current_score += 1
        print(f"You're right! Current score: {current_score}\n")
    elif choice == "B" and second_followers > first_followers:
        current_score += 1
        first_number = second_number
        print(f"You're right! Current score: {current_score}\n")
    else:
        game = False
        final_score = current_score
        print(f"You're wrong! Final score: {final_score}")
