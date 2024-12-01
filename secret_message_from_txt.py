import string
#examples are simple encryption and decryption schemes
import nltk
#national language toolkit
nltk.download("words")
from nltk.corpus import words
words = words.words()



f = open('secret_message.txt', 'rb')
ciphertext = f.read().decode('ascii')
f.close()
# ciphertext now contains the text from the file


def caesar_encryt(message, shift):
    """
    Encrypt a message using a caesar cipher
    :param message: clear (plain) text message
    :param shift: key for the caesar cipher
    :return: cipher text (encrypted message)
    """

    #stat with a blank string
    ciphertext = ""
    #string containing all of the printable charcters in python
    alphabet = string.printable

    #iterate over all characters in our message
    for c in message:
        #shift c by the key amount
        #find location of c in the alphabet

        cpos = alphabet.find(c)
        #add shift amount to this location
        #mod by length of alphabet to the start of the letters
        cipherpos = (cpos + shift) % len(alphabet)

        #append the character from the alphabet at this location to our cipher text
        ciphertext += alphabet[cipherpos]

    return ciphertext

def caesar_decrypt(ciphertext, shift):


    return caesar_encryt(ciphertext, -shift)










#crack the key
#there is only as many keys then they are letters in alphabet
for i in range(len(string.printable)):
    #tries the current key
    print(i, caesar_decrypt(ciphertext, i))

#use the natural language toolit to try to crack this code

best_key = -1
best_total = 0

for i in range(len(string.printable)):
    total = 0
    text = caesar_decrypt(ciphertext, i)
    #split this string on spaces
    sentence = text.split()
    for word in sentence:
        #check if the word is in our list of words from the nltk
        #check if the lower case version of the word is in ntlk
        if word in words or word.lower() in words:
            total += 1
    #check is this total is better than our last
    if total > best_total:
        best_total = total
        best_key = i
        print("Current best:", i, text)

print("Final Answer:", caesar_decrypt(ciphertext, best_key))

f = open("cracked_secret_message.txt", "w")

#write method allows is to write/output a string to a file
f.write("St. Lawrence University was founded on April 3, 1856")
#when done we need to close file
f.close()
