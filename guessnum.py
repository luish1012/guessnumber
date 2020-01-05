import random

value = random.randint(0, 3)
print(value)
guess = int(input("Enter an int from 0 to 3: "))

while value != "guess":
    print
    if guess < value:
        print("Guess is too low dumbass")
    elif guess > value:
        print("Guess is too high")
    else:
        print("correct")





    #
# while phrase != "quit":
#     phrase = input ('Guess the number!')
#     print (f"What you entered is {len(phrase)} characters long")


# guess = input ('Guess the number: ')
# if guess == value:
#     print('You guess correct!')
# else:
#     print('Incorrect!')
