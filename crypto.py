#examples are simple encryption and decryption schemes
import string
import nltk
import random
import util
#national language toolkit
nltk.download("words")

from nltk.corpus import words

words = words.words()


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
def substitute_encrypt(message, key):
    """
    Encrypt a message with a substitution cipher
    :param message: clear text message
    :param key: scramble alphabet
    :return: ciper text (encryted message)
    """
    alphabet = string.printable
    ciphertext = ""
    for c in message:
        #perform substitution
        #look up the position of c in out alphabet
        cpos = alphabet.find(c)
        #add the letter from key at the same position to ciphertext
        ciphertext += key[cpos]
    return ciphertext

def substitute_decrypt(ciphertext, key):
    alphabet = string.printable
    cleartext = ""
    for c in ciphertext:
        #look up the pos of c in our **key**
        cpos = key.find(c)
        cleartext += alphabet[cpos]
    return cleartext


def otp_encrypt(message, key):
    """
    Encryp a message with one time pad (unbreakable)
    :param message: clear text
    :param key: random string that is the msame length as our message
    :return: cipher text (encrypted message)
    """
    alphabet = string.printable
    ciphertext = ""
    #loop through the indices of our string
    for i in range(len(message)):
        #pull out one character from the message and one from the key
        message_c = message[i]
        key_c = key[i]
        #grad the position of both from our alphabet
        m_pos = alphabet.find(message_c)
        k_pos = alphabet.find(key_c)
        #add these two positions together (mod by length alphabet)
        #to find the position of the encrypted letter
        cipher_pos = (m_pos + k_pos) % len(alphabet)
        #add this letter to the cipher
        ciphertext += alphabet[cipher_pos]
    return ciphertext

def otp_decrypt(ciphertext, key):
    """
    Encryp a message with one time pad (unbreakable)
    :param message: clear text
    :param key: random string that is the msame length as our message
    :return: cipher text (encrypted message)
    """
    alphabet = string.printable
    cleartext = ""
    #loop through the indices of our string
    for i in range(len(ciphertext)):
        #pull out one character from the message and one from the key
        cipher_c = ciphertext[i]
        key_c = key[i]
        #grad the position of both from our alphabet
        cipher_pos = alphabet.find(cipher_c)
        k_pos = alphabet.find(key_c)
        #add these two positions together (mod by length alphabet)
        #to find the position of the encrypted letter
        message_pos = (cipher_pos - k_pos) % len(alphabet)
        #add this letter to the cipher
        cleartext += alphabet[message_pos]
    return cleartext



#amin prog
message = "Dana Brunch @ Noon"
key = random.randrange(len(string.printable))
encrypted = caesar_encryt(message, key)
decrypted = caesar_decrypt(encrypted, key)
print(encrypted)
print(decrypted)

#crack the key
#there is only as many keys then they are letters in alphabet
for i in range(len(string.printable)):
    #tries the current key
    print(i, caesar_decrypt(encrypted, i))

#use the natural language toolit to try to crack this code

best_key = -1
best_total = 0

for i in range(len(string.printable)):
    total = 0
    text = caesar_decrypt(encrypted, i)
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

print("Final Answer:", caesar_decrypt(encrypted, best_key))

#substitution cipher
substitution_key = util.scramble(string.printable)
encrypted = substitute_encrypt(message, substitution_key)
decrypted = substitute_decrypt(encrypted, substitution_key)
print("Encryption with substitution cipher", encrypted)
print("Decryption with substitution cipher", decrypted)

#one time pad
#to use this we need a key
#we need to generate a string of random letters the same length as our message
otp_key = ""
for i in range(len(message)):
    #pick a random letter
    #MAJOR SECURITY FLAW
    #random gives us pseudo random numbers meaning it is possible to detect and guess the pattern of random numbers being generated
    #we need random numbers that are truly random which are crypographically secure
    #in python, we can use the "secrets" module instead of "random"
    letter = string.printable[random.randrange(len(string.printable))]
    otp_key += letter

encrypted = otp_encrypt(message, otp_key)
decrypted = otp_decrypt(encrypted, otp_key)
print("Encrytion with otp:", encrypted)
print("Decrytion with otp:", decrypted)

#write the encrypted message to a file
f = open("encrypted_message.txt", "w")

#write method allows is to write/output a string to a file
f.write(encrypted)
#when done we need to close file
f.close()
