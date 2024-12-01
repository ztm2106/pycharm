#user has to guess the correct word from a collection of letters

import util

#list of tagert words

#words = ["Minh", "Minh", "Minh", "Minh"]

#lets read in the words from word.txt
words = []
#open the word file
f = open("words.txt")
for line in f:
    #remve the extra new line
    word = line.strip()
    #add the word to our list
    words.append(word)
f.close()


#for loop to iterate over the words in the list
for word in words:
    #target word
    #word = "elephant"

    #get a scrambled version of this
    scramble = util.scramble(word)

    #game logic
    print("Guess the word formt his set of scrambled letters: ", scramble)
    guess = input("Enter a quess: ")

    if guess == word:
        print("Hooray")
    else:
        print("try again next time")

        exit()



























