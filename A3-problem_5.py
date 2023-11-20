# Problem 5
# cracking encrypted message
# Darshana Venkatadasan

from problem3 import caesar_decrypt
# from problem4 import *

valid_keys = []
# ciphertext
ciphertext = "FRQJUDWXODWLRQV RQ WDNLQJ BRXU ILUVW FRPSXWHU VFLHQFH HADP".lower()
# Assume the key is a number between 1 and 25
for key in range(1, 26):
    # Decrypt the ciphertext using the key
    plaintext = caesar_decrypt(key, ciphertext)
    
    # Print the plaintext
    print(f"Key: {key}, Plaintext: {plaintext}")

    # check if any word is one of the words in common_words.txt
    for word in plaintext.split():
        if word in items:
            if not key in valid_keys:
                valid_keys.append(key)

# in the end, share valid keys
print("The valid keys are:")
print(valid_keys)
