#make a list of words
#pick a random word
#draw spaces
#take guess
#draw guessed letters and strikes
#print out win/lose

import random

words = [
    'apple',
    'banana',
    'orange',
    'stawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon',

    ]
print(words)
while True:
    start = input("Press enter/return to start or Q to quit")
    if start.lower() == 'q':
        break

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print('')
        print('strikes: {}/7'.format(len(bad_guesses)))
        print('')


        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter! ")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed that letter! ")
            continue
        elif not guess.isalpha():
            print("You can only guess letters! ".format(secret_word))
            continue
        
            
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break

        else:
            bad_guesses.append(guess)

    else:
        print("You didn't guess it! my secret word was {} ".format(secret_word))
            
