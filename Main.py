import Words
import random

play = True

while play:
    solution = random.choice(Words.words)
    print(solution)
    win = False
    tries = 6
    
    while tries > 0 and not win:

        if tries == 1:
            print("You have", str(tries), "try remaining!\n")
        else: 
            print("You have", str(tries), "tries remaining!\n")

        guessing_a_word = True

        while guessing_a_word:
            guess = input("Guess a 5 letter word: ")
            if guess == solution:
                win = True
                break
            if len(guess) == 5:
                if guess in Words.words:
                    guessing_a_word = False
                else:
                    print("Guess not in word list!")
                    continue
            else:
                print("Guess must contain 5 letters!") 
        
        for i in range(5):
            if guess[i] == solution[i]:
                print(guess[i] + " - Green")
            elif guess[i] in solution:
                print(guess[i] + " - Orange") 
            else:
                print(guess[i] + " - Incorrect")
        
        tries -= 1

    if win:
        print("You WIN!")
    else:
        print("You LOSE!")

    play_again = input("Play again? Y/N: ").upper()
    if play_again  == "Y":
        continue
    elif play_again == "N":
        play = False  
        
