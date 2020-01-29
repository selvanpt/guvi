import random
a = random.randrange(1, 10)
guess = int(input("Please enter your guess: "))
 
if guess == a:
    print ("Hit!")
elif guess < a:
    print ("Your guess is too low")
else:
    print ("Your guess is too high")
