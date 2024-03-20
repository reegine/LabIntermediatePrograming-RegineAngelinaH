import os
# Clearing the Screen
os.system('cls')

# Tuliskan sebuah program yang meminta user memasukan umurnya, lalu memberikan output umur user tersebut 50 tahun yang akan datang. 
# Pastikan input diantara 0 - 150. Format output agar menampilkan 3 digit angka. 

# while True :
#     user_input = int(input('Enter your current age (range of age is between 1-150 years) : '))
#     if 1 <= user_input <=150 :
#         count = user_input + 50
#         print('This is your age after 50 years :', count)
#         break
#     else :
#         print('input a number between 1-150')

'''
Hangman part 1.

Simpan sebuah kata dalam variable (kata rahasia).
Minta user untuk memberikan sebuah huruf.
Pastikan user memberikan input yang valid (satu buah huruf)
Periksa apakah huruf yang diberikan user ada dalam kata rahasia anda dengan mengabaikan kapitalisasi huruf. 
'''

def updateText(secret_word,display_text, guess):
    updated_text = ""
    for i in range(len(secret_word)):
        if secret_word[i].lower() == guess.lower() :
            updated_text += guess.lower()
        else :
            updated_text += display_text[i]
    return updated_text
    

def hangman(word) :
    secret_word = word.lower()
    print("ini yg secret word", word)
    chances = 7
    inputted = ""
    display_text = "_" * len(secret_word)
    print('you have ', chances, " chances to guess")
    print(display_text)
    
    while chances > 0 :
        user_input = input('\nGuess a letter : ').lower()
        if len(user_input) == 1 :
            if user_input in inputted :
                print('you already guessed the letter, guess another letter')
                # print(inputted)
            elif user_input in secret_word :
                inputted += user_input.lower()
                if user_input.lower() in secret_word.lower() :
                    print('you guessed a letter correct!')
                    display_text = updateText(secret_word,display_text,user_input)
                    print(display_text)
            else :
                chances -= 1
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
                print("\n",display_text)
        else :
            print('Incorrect amount of  characters')
        
    if "_" not in display_text:
        print('Congratulations! You guessed the word The word was:', secret_word)

    if chances == 0 :
        print('Sorry, you ran out of chances. The word was:', secret_word)


print('Welcome To Hangman :D !!\n')
hangman('PUDDING')