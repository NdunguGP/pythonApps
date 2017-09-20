import random


print("-------------------------------------------------")
print("               GUESS THE NUMBER APP ")
print("-------------------------------------------------")


num = random.randint(0, 100)


while True:
    guess = int(input("Enter a number between 0 and 100 "))




    if guess < num:
        print("Sorry but {} is lower than the number".format(guess))
        
    if guess > num:
        print("Sorry but {} is higher than the number".format(guess))
        
    if guess == num:
        print("Yes! you got it. The number was {}".format(num))
        break

