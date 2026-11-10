import random
playing = True
number = random.randint(1,10)
print("I have thought of a number, try to guess it")
while playing:
    try:
        guess = int(input("Enter a number:"))
    except:
        print("Not a valid inpur, try again!")
    else:
        if number == guess:
            print("You have guessed the correct number!")
            playing = False
        elif guess > number:
            print("You have guessed very high, make a lower guess.")
        elif guess < number:
            print("You have guessed very low, make a higher guess.")
        else:
            print("wrong guess, Try Again")