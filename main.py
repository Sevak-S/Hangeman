"""
Game Hangman
This game was created by Sevak Khachatryan
If you find any bugs please write on email example@example.com
"""

import random
import string
from words_example import examples


def get_valid_word(words):
    """
    the function getting random word from python file words
    :param words:
    :return: word
    """
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    """
    the function check a letters and lives
    :return: result
    """
    word = get_valid_word(examples)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd'])  -->'a b cd'
        print('You have', lives, 'lives left and you have used these letters: \
         ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters
                     else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1  # take away life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guess the word', word, '!!')


if __name__ == '__main__':
    hangman()
