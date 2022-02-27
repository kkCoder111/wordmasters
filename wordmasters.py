# Author - kkCoder111
import random

# Source of words
words = [
    "areas",
    "vivid",
    "words",
    "super",
    "ultra",
    "birds",
    "angry"
    #TODO: Add more words
]


guesses = 0
ans = random.choice(words)
ansSplit = []
for i in range(len(ans)):
    ansSplit.append(ans[i])
def checkWord(word):
    global guesses
    wordList = []
    if len(word) > 5:
        print("Too many digits!")
    elif len(word) < 5:
        print("No word entered or too less digits")
    else:
        guesses += 1
        for i in range(len(word)):
            wordList.append(word[i])
        for i in range(len(word)):
            if wordList[i] == ansSplit[i]:
                print("Letter", str(i+1) + ":", "Correct letter and place")
            else:
                if wordList[i] in ansSplit:
                    print("Letter", str(i+1) + ":", "Correct letter, wrong place")
                else:
                    print("Letter", str(i+1) + ":", "Wrong letter")
while guesses < 6:
    print("Remaining guesses:", str(6-guesses))
    guess = input("Enter a 5-letter word:")
    checkWord(guess)
    if guess == ans:
        guesses = 6
        guessed = True

if guessed:
    print("Good work!")

else:
    print("Better luck next time!")
    
print("Thanks for playing WordMasters!")
