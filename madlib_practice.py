import random

print("Lets Learn about stuff")
def game():
    name = input("What is your name: ")
    favorite_food = input("What is your favorite food: ")
    favorite_animal = input("What is your favorite animal: ")

    words = []
    words.append(name)
    words.append(favorite_food)
    words.append(favorite_animal)

    print(f'hello {name} I learned your favorite food is {favorite_food} and your favorite animal is {favorite_animal}.')
    print("*")
    print(f'hello {random.choice(words)} I learned your favorite food is {random.choice(words)} and your favorite animal is {random.choice(words)}.')
    user_input = input("Do you want to play again? y or n: ")
    if user_input=="y":
        game()
    else:
        print("\nThank you for learning with me byeeee!!")

game()