import os
import random
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

secretwordlist = ["pudding", "gulali", "Lampu", "Banana", "IKAN"]
scorehistoryWIN = 0
scorehistoryLOSE = 0


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
    # print("ini yg secret word", word)
    # print("ini isi yg list", secretwordlist)
    chances = 7
    inputted = ""
    display_text = "_" * len(secret_word)
    print('you have ', chances, " chances to guess")
    print(display_text)
    
    while chances > 0 and "_" in display_text :
        global scorehistoryWIN, scorehistoryLOSE
        user_input = input('\nGuess a letter : ').lower()
        if len(user_input) == 1 and user_input.isalpha() :
            if user_input in inputted :
                print('you already guessed the letter, guess another letter\n')
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
            print("Make sure you only input one characters which is an alphabet\n")

    if "_" not in display_text :
        scorehistoryWIN = scorehistoryWIN + 1
        print('\nCongratulations! You guessed the word The word was:', secret_word)    
        print('You won : ', scorehistoryWIN)  
        print('You lost : ', scorehistoryLOSE, "\n")  
        
    if chances == 0 :
        scorehistoryLOSE = scorehistoryLOSE + 1
        print('Sorry, you ran out of chances. The word was:', secret_word)
        print('You won : ', scorehistoryWIN)  
        print('You lost : ', scorehistoryLOSE, "\n")   

def main() :
    while True : 
        if secretwordlist == [] :
            print("Congradulations!!\nYou have guessed all the word's I could think of :D")
            break
        else : 
            print('Welcome To Hangman :D !!\n')
            play = input("Do you want to play Hangman? (y/n): ").lower()
            if play == "y" or play == "yes"  : 
                # print("ini yg index print ",random.randint(0,len(secretwordlist)))
                pickedword = secretwordlist[random.randint(0,len(secretwordlist))]
                secretwordlist.remove(pickedword)
                hangman(pickedword)
                continue  
            elif  play == "n" or play == "no" :
                print("See you next time")
                break
            else : 
                print("Please only input either y or n\n")
                continue   

main()