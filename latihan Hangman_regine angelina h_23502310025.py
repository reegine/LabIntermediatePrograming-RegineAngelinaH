import os

# Clearing the Screen
os.system('cls')

#Regine Angelina Halim | 23502310025

'''
Hangman part 1.

Simpan sebuah kata dalam variable (kata rahasia).
Minta user untuk memberikan sebuah huruf.
Pastikan user memberikan input yang valid (satu buah huruf)
Periksa apakah huruf yang diberikan user ada dalam kata rahasia anda dengan mengabaikan kapitalisasi huruf. 
'''

def hangman() :
    secret_word = 'pudding'
    temp = secret_word
    chances = 7
    inputted = set()
    print('you have ', chances, " chances to guess")
    
    while chances > 0 and set(secret_word):
        user_input = input('Guess a letter : ').lower()
    
        if len(user_input) == 1 :
            if user_input in inputted :
                print('you already guessed the letter, guess another letter')
                # print(inputted)
            elif user_input in secret_word :
                secret_word = secret_word.replace(user_input, '')
                inputted.add(user_input)
                print('you guessed a letter correct!')
                # print(secret_word)
            else :
                chances = chances-1
                print('Try again!\nyou have', chances, "chances left")
                print("This Is Your Hangman\n")
                if chances == 6 :
                    print("  ( )")
                elif chances == 5:
                    print("  ( )")
                    print("  /|\ ") 
                elif chances == 4:
                    print("  ( )")
                    print("  /|\ ") 
                    print("  / \ ") 
                elif chances == 3:
                    print("   |")
                    print("  ( )")
                    print("  /|\ ") 
                    print("  / \ ") 
                elif chances == 2:
                    print("____")
                    print("   |")
                    print("  ( )")
                    print("  /|\ ") 
                    print("  / \ ") 
                elif chances == 1:
                    print("____")
                    print("|  |")
                    print("| ( )")
                    print("| /|\ ") 
                    print("| / \ ") 
                    print("|")
                elif chances == 0 :
                    print("____")
                    print("|  |")
                    print("| ( )")
                    print("| /|\ ") 
                    print("| / \ ") 
                    print("|")
                    print("--------")
        else :
            print('Incorrect amount of  characters')

    if not set(secret_word):
        print('Congratulations! You guessed the word The word was:', temp)  
    else:
        print('Sorry, you ran out of chances. The word was:', temp)

print('Welcome To Hangman :D !!\n')
hangman()