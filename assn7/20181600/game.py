from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('assn7/words.txt')
    try:
        guess = Guess(word.random_word())
    except ValueError:
        print('can\'t find words.txt')
        exit()
    is_finished = False
    hangman = Hangman()
    max_tries = hangman.get_life()

    while guess.num_tries < max_tries:

        display = hangman.get(max_tries - guess.num_tries)
        print(display)
        guess.display()

        guessed_char = input('Select a letter: ')
        guessed_char = guessed_char.lower()
        if not guessed_char.isalpha():
            print('Input alphabet')
            continue
        if len(guessed_char) != 1:
            print('One character at a time!')
            continue
        if guessed_char in guess.guessed_chars:
            print('You already guessed \"' + guessed_char + '\"')
            continue

        is_finished = guess.guess(guessed_char)
        if is_finished:
            break

    if is_finished:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secret_word + ']')
        print('guess [' + guess.current_status + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
