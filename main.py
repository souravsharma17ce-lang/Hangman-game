print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
""")

import random   #pick a random number
words = ["words","python","fruit","banana","strawberry"]  #create a list of words
chosen_word = random.choice(words)

guessed_letter = [] #create a blank list
for letter in chosen_word:  
    guessed_letter.append("_")
print(guessed_letter) 

lives = 6 #set a number of lives

print("🎮welcome to Hangman🎮")
score = 0
while lives>0 and "_"in guessed_letter:  #game loop
    print("\nword:"," ".join(guessed_letter))
    guess = input("Guess a letter:").lower()

    if guess in guessed_letter:  #WARN IF ALREADY GUESS
        print(f"⚠️you already guessed {guess}")
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("❌please enter a single letter!")
        continue


    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                guessed_letter[i] = guess #if letter match then updated in guessed_letter
                score+=10
        print(f"correct guess✅ and your score is {score}")

    else:
        lives -=1
        print("wrong guess!")
        print("lives left", "❤️  " *lives)
        score-=10
        print(f"your score is {score}")


if"_" not in guessed_letter:
    print("\n you win 🎉 the word was:",chosen_word)
else:
    print("\n you loose💀the word was:",chosen_word)




  
 












