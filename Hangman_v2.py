import random
from datetime import datetime
import pandas as pd

random.seed(datetime.now())

class library():

    game_dictionary = pd.read_csv('hangmanV2.csv')

    def request_word():
        df = self.game_dictionary.sample(random_state = random.randint(1,100)).values.tolist()
        return df[0][0].lower(), df[0][1]
       
    def add_words():
        print("Enter a word with no symbols and no numbers. Enter a clue delimited by comma(,). \n")
        
        try:
            words = [word for word in input("> ").split(',')]
        except ValueError:
            print("Something went wrong. Please try again. \n")
            HangmanMain.Menu()
        
        if not all(x.isalpha() or x.isspace() for x in words[0]):
                print("The entered word contains non-alphabetic character(s). Try again. \n")
                HangmanMain.Menu()
            
        df = pd.DataFrame(data = words).T
        df.columns = ['word', 'clue']

        self.game_dictionary = self.game_dictionary.append(df)

        print("{} has been added to the Pandora's Box \n".format(df.loc[0, 'word']))

        self.game_dictionary.to_csv('hangmanV2.csv', index = False)
        HangmanMain.Menu()

class HangmanGame():

    lives = 6

    def hangman_animation(still_guessing, guessed):

        if still_guessing:
            if self.lives == 0:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  | -\__(^^)__/-\n"
                      "  |      /\     \n"
                      "  |      \/     \n"
                      "  |      /\     \n"
                      "  |     /  \    \n"
                      "  |             \n"
                      "__|__\n")
                
            elif self.lives == 1:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  | -\__(^^)__/-\n"
                      "  |      /\     \n"
                      "  |      \/     \n"
                      "  |      /      \n"
                      "  |     /       \n"
                      "  |             \n"
                      "__|__\n")
                
            elif self.lives == 2:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  | -\__(^^)__/-\n"
                      "  |      /\     \n"
                      "  |      \/     \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "__|__\n")
                
            elif self.lives == 3:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  | -\__(^^)__/-\n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "__|__\n")
                
            elif self.lives == 4:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  | -\__(^^)    \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "__|__\n")
                
            elif self.lives == 5:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  |     (^^)    \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "__|__\n")
            
            elif self.lives == 6:
                print("   ___________  \n"
                      "  |      |      \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "  |             \n"
                      "__|__\n")

        elif not guessed:
            print("                \n"
                  "       _ _      \n"
                  "     ~( ^ )~    \n"
                  "                \n"
                  "   ___________  \n"
                  "  |      |      \n"
                  "  |             \n"
                  "  |             \n"
                  "  |  \n")

        elif guessed:
            print("   ___________  \n"
                  "  |      |      \n"
                  "  |             \n"
                  "  |             \n"
                  "  |   _(^^)_    \n"
                  "  |  /  /\  \   \n"
                  "  |  \_ \/ _/   \n"
                  "  |     /\      \n"
                  "__|___ /__\____ \n")
        else:
            print("You did something not expected by my program. Datsy you don't get a stickman!")
            
    def initialize():
        print("Welcome to Command-line Hangman \n")
        print("You have 6 lives to figure out the word. You can take the help of the clue provided. \n")

    def play():

        guessword, clue = library.request_word()
        guessed = False
        guessed_letters = []
        still_guessing = True
        word_state = "_ " * len(guessword)
        space_index = [n for n, i in enumerate(guessword) if i.isspace() == True]
        for spaces in space_index:
            word_state = word_state[:spaces*2] + ' ' + word_state[spaces*2+1:]

        print('Clue: {} \n'.format(clue))
        print("Start guessing... \n")
        self.hangman_animation(still_guessing, guessed)
        print(word_state)

        while not guessed and self.lives > 0:
            guess = input('> ').lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You've already tried this letter. Your list of guessed letters include {} \n".format(guessed_letters))

                elif guess not in guessword:
                    self.lives -= 1
                    self.hangman_animation(still_guessing, guessed)
                    print("Oopsies! {} is not in the word. Try again".format(guess))
                    print(word_state)
                    guessed_letters.append(guess)
                    if self.lives == 0:
                        still_guessing = False

                else:
                    print("Right on! {} is in the word \n".format(guess))
                    temp_list = list(word_state)
                    letter_index = [i for i, letter in enumerate(guessword) if letter == guess]
                    for index in letter_index:
                        temp_list[index*2] = guess
                    word_state = "".join(temp_list)
                    print(word_state)
                    if "_" not in word_state:
                        guessed = True
                        still_guessing = False
                    guessed_letters.append(guess)

            else:
                print("InputError Raised! Invalid input. Enter a character. \n")

        if guessed:
            print("Bingo! You guessed the word. \n")
            self.hangman_animation(still_guessing, guessed)
        else:
            print("Unlucky. You ran out of lives. The word was {} \n".format(guessword))
            self.hangman_animation(still_guessing, guessed)

        self.lives = 6
        HangmanMain.Menu()

class HangmanMain():

    def Menu():
        print("1 > Start Game \n"
              "2 > Add New Words \n"
              "3 > Quit \n"
              )

        valid_inputs = {1: self.Hangman,
                        2: library.add_words,
                        3: quit
                        }

        invalid_selection = True

        while invalid_selection:
            try:
                selected_option = int(input("> "))
            except ValueError:
                print("ValueError Raised! Enter a number from the options given. \n")
                continue

            if selected_option not in valid_inputs:
                print("Enter an option number from menu.")
            else:
                invalid_selection = False

        valid_inputs[selected_option]()
        print('\n')

    def Hangman():
        HangmanGame.initialize()
        HangmanGame.play()

if __name__ == "__main__":
    HangmanMain.Menu()
