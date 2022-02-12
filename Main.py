import Words
import random

solution = random.choice(Words.words)

guessing_a_word = True
while guessing_a_word:
    guess = input("Guess a 5 letter word: ")
    if len(guess) == 5:
        if guess in Words.words:
            guessing_a_word = False
        else:
            print("Guess not in word list!")
            continue
    else:
        print("Guess must contain 5 letters!") 
    


#take user input 
#is this letter in the word
#is it in the right position