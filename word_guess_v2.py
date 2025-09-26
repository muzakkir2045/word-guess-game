""" == Word Guessing Game == """

import random

words = '''apple banana mango strawberry orange grape pineapple apricot 
lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
word = random.choice(list(map(lambda fruit : fruit.strip("\n"),words.split(' ')))).lower()
guesses = ''

for turn in range(len(word)+2):
    for ch in word:
        print(ch if ch in guesses else "_",end=" ")
    guess = input("\nEnter a character : ")
    guesses += guess
    if guess not in word:
        print("\nWrong")
    elif all(ch in guesses for ch in word):
        print("Hooray! You Won!")
        break
else:
    print(f"You loose!\nThe word was {word}")
    print("Better luck next time!")
