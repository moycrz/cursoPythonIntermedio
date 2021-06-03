import random
import os
import hangman_art


def hangman():   
    with open("./data/data.txt", "r", encoding="utf-8") as f:
        word_list = [i for i in f]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word) - 1
    end_of_game = False
    lives = 6

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                os.system("cls")
                print(hangman_art.logo)
                display[position] = letter

        if guess not in chosen_word:
            os.system("cls")
            print(hangman_art.logo)
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"\nYou lose, the word was {chosen_word}.")

        print(f"{' '.join(display)}")
        
        if "_" not in display:
            end_of_game = True
            os.system("cls")
            print(hangman_art.logo)
            print(f"\nYou won, the word was {chosen_word}.")
        print(hangman_art.stages[lives])
        

def run():
    os.system("cls")
    print(hangman_art.logo)
    hangman()


if __name__ == "__main__":
    run()