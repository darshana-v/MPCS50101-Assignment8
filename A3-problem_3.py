# Problem 3
# caesar cipher encryption and decryption
# Darshana Venkatadasan

def caesar_encrypt(key, message):
    # Create an empty string to store the encrypted message
    encrypted_message = ""
    
    for character in message:
        # Get the ASCII value of the character
        ascii_value = ord(character)
        
        # If the character is a letter, shift it by the key
        if character.isalpha():
            if character.islower():
                # Shift the character by the key
                ascii_value += key
                # loop back to the start of the alphabet
                if ascii_value > ord('z'):
                    ascii_value -= 26

            else:
                # Shift the character by the key
                ascii_value += key
                # loop back to the start of the alphabet
                if ascii_value > ord('Z'):
                    ascii_value -= 26

        encrypted_message += chr(ascii_value)
    return encrypted_message


def caesar_decrypt(key, message):
    # Create an empty string to store the decrypted message
    decrypted_message = ""
    
    for character in message:
        # Get the ASCII value of the character
        ascii_value = ord(character)
        
        if character.isalpha():
            # Check if the character is lowercase
            if character.islower():
                # Shift the character by the key
                ascii_value -= key
                # loop back to the end of the alphabet
                if ascii_value < ord('a'):
                    ascii_value += 26

            else:
                # Shift the character by the key
                ascii_value -= key
                # loop back to the end of the alphabet
                if ascii_value < ord('A'):
                    ascii_value += 26
        
        decrypted_message += chr(ascii_value)
    return decrypted_message

def start_cipher():
    technique = input("Do you want to encrypt/decrypt a message or view an example?: ")
    if(technique == "encrypt"):
        s = input("Enter plaintext: ")
        try:
            key = int(input("Enter key value: "))
            print(f"Encrypted message is: {caesar_encrypt(key, s)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif (technique == "decrypt"):
        s = input("Enter ciphertext: ")
        try:
            key = int(input("Enter key value: "))
            print(f"Decrypted message is: {caesar_decrypt(key, s)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif (technique == "example"):
        s = "Experience is the teacher of all things"
        key = 12
        print(f"Example plaintext is: {s}")
        print(f"Key is: {key}")
        print(f"Ciphertext: {caesar_encrypt(key, s)}")

    elif (technique == "exit"):
        exit

    else:
        print("Please enter 'encrypt' or 'decrypt' to encrypt or decrypt a message, 'example' to view an example or 'exit' to exit the program:")
        start_cipher()

if __name__ == "__main__":
    start_cipher()       
