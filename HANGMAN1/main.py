
import random

with open('easyword.txt', "r") as word_list:
    word_list_1 = list(word_list)
with open('normalword.txt', "r") as word_list:
    word_list_2 = list(word_list)
with open('wordlist.txt', "r") as word_list:
    word_list_3 = list(word_list)

def get_word_1(word_list_1):
    word = random.choice(word_list_1)
    return word.upper()

def get_word_2(word_list_2):
    word = random.choice(word_list_2)
    return word.upper()

def get_word_3(word_list_3):
    word = random.choice(word_list_3)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " ist nicht das Wort :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")




def display_hangman(tries):
    stages = [  """
                   ♡♡♡♡♡♡
                   """,
                   """
                   ♥♡♡♡♡♡
                   """,
                   """
                   ♥♥♡♡♡♡
                   """,
                   """
                   ♥♥♥♡♡♡
                   """,
                   """
                   ♥♥♥♥♡♡
                   """,
                   """
                   ♥♥♥♥♥♡
                   """,
                   """
                   ♥♥♥♥♥♥
                   """
    ]
    return stages[tries]

def main():

    mode = input("CHOOSE YOUR PLAY MODE PRESS: \nEASY \nNORMAL \nHARD \nRIGHT YOUR CHOOSE:").upper()

    if mode == "EASY":
        word = get_word_1(word_list_1)
        play(word)
        while input("Again? (Y/N) ").upper() == "Y":
            main()
    elif mode == "NORMAL":
        word = get_word_2(word_list_2)
        play(word)
        while input("Again? (Y/N) ").upper() == "Y":
            main()
    elif mode == "HARD":
        word = get_word_3(word_list_3)
        play(word)
        while input("Again? (Y/N) ").upper() == "Y":
            main()
    else:
        print("something went wrong please make sure you choose the mode correctly")
        main()

if __name__ == "__main__":
    main()
