
import random

MAX_GUESSES = 10
NUM_DIGITS = 3


def main():
    print('''This is a letter game that i crated the rules are simple i i put them below


####################################################################
When I say:        That means:
Pico               One letter is correct but in the wrong position.
Fermi              One letter is correct and in the right position.
Bagels              No letter is correct.
####################################################################
     
 
     ''')

    while True:
        secretLetter = getSecretLetter()
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretLetter)
            print(clues)
            numGuesses += 1

            if guess == secretLetter:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretLetter))
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')


def getSecretLetter():
    letters = list('aeiou')
    random.shuffle(letters)
    secretLetter = ''
    for i in range(0, NUM_DIGITS):
        secretLetter += str(letters[i])
    return secretLetter


def getClues(guess, secretLetter):
    if guess == secretLetter:
        return 'You got it!'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretLetter[i]:
            clues.append('Fermi')
        elif guess[i] in secretLetter:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        clues.sort()
        return ' '.join(clues)


 # If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
