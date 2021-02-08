from random import randint

print("Guess a number!\nThe upper and lower bound cannot be the same\n")
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))


res = randint(lower, upper) #Generate the number what we have to guess
print("\n")


guesslimit = round((upper - lower)/2) #Maximum guesses limit
print("Your guess limit is " + str(guesslimit))

counter = 0
while counter < guesslimit:
    counter += 1
    print("Number of guess: " + str(counter))
    num = int(input("Guess: "))
    if num == res:
        print("Congratulations, you guessed right")
        break
    elif num < lower or num > upper:
        print("You can't guess outside of the range")
    elif num < res:
        print("No, your guess is too small. Please try again\n")
    elif num > res:
        print("No, your guess is too big. Please try again\n")

if counter > guesslimit:
    print("Sorry you ran out of the guesses")