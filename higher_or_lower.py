import random
from art import higher_lower, vs
from game_data import data
print(higher_lower)


def play_again():
    print("Do You want to try again? Type 'Y' or 'N':\n")
    answer = input().lower()
    if answer == 'y':
        keep_playing()
    elif answer == 'n':
        print("Thanks for the play.")
        quit()
    else:
        print("Something gone wrong. Try again.")


def keep_playing():

    random_person_a = random.choice(data)
    random_person_compare_a = random_person_a['follower_count']

    random_person_b = random.choice(data)
    random_person_compare_b = random_person_b['follower_count']

    score = 0

    correct_answer = True

    while correct_answer:
        print(f"""Compare A: {random_person_a['name']}, a {random_person_a['description']}, from {random_person_a['country']}.
        """)

        print(vs)

        print(f"""Compare B: {random_person_b['name']}, a {random_person_b['description']}, from {random_person_b['country']}.
        """)

        user_answer = input("Who have got more followers on Instagram? Type 'A' or 'B'\n").lower()

        if user_answer == 'a':
            if random_person_compare_a > random_person_compare_b:
                score += 1
                print(f"Correct. Score {score}.")

                random_person_a = random_person_b
                random_person_compare_a = random_person_compare_b

                random_person_b = random.choice(data)
                random_person_compare_b = random_person_b['follower_count']

            elif user_answer:
                correct_answer = False
                print(f"Sorry, that's wrong. Your final score is {score}")
                play_again()

        if user_answer == 'b':
            if random_person_compare_b > random_person_compare_a:
                score += 1
                print(f"Correct. Score {score}.")

                random_person_a = random_person_b
                random_person_compare_a = random_person_compare_b

                random_person_b = random.choice(data)
                random_person_compare_b = random_person_b['follower_count']

            elif user_answer:
                correct_answer = False
                print(f"Sorry, that's wrong. Your final score is {score}")
                play_again()


keep_playing()
