import os
import random
# Clearing the Screen
os.system('cls')

''' Read from the text file "alice.txt"​
Count how many words, and how many unique words in the text.​
Find all misspelled words, by comparing with "words.txt".​
Assume that "words.txt" contains all correctly spelled words.​ '''

# 1. opens the text file
alice_file = open("D:\Prasmul\Pelajaran\Semester 2\Intermediate Programming\Tugas Kumpul\LabIntermediatePrograming-RegineAngelinaH\Tugas Lab 5\Alice.txt", "r")
full_file_alice = alice_file.read()
# print(alice_file.read())

# 2. count how many words = 28190 
# many_words = len(full_file_alice)
words_alice = full_file_alice.split()
many_words_alice = len(words_alice)
print("ini yg many words",many_words_alice)

# 3. count unique words
set_words_alice = set(words_alice)
many_unique_words = len(set_words_alice)
print("ini yg many unique words",many_unique_words)

# 4. find all misspelled words, by comparing with words.txt
words_file = open("D:\Prasmul\Pelajaran\Semester 2\Intermediate Programming\Tugas Kumpul\LabIntermediatePrograming-RegineAngelinaH\Tugas Lab 5\words.txt", "r")
full_file_words = words_file.read()
words_words = full_file_words.split()
set_words_words = set(words_words)
many_words_words = len(set_words_words)
# difference = set_words_words - set_words_alice

difference = []
for i in set_words_alice:
    if i not in set_words_words:
        difference.append(i)

print("ini yang difference between alice and words file\n\n", difference)
print("\n\nini banyak kata yang berbeda\n", len(difference))

# 5. closes the text file
alice_file.close()
words_file.close()
