'''
Evangeline Kim
Oct. 22nd, 2023
Code to decrypt any Caesar Cipher code through the brute force method.
'''

def decrypt_caesar_cipher(encrypted_message):
    '''Function decrypt_caesar_cipher takes an encrypted message and runs it through all 26 possible caesar cipher shifts.
    Parameters: The encrypted message (a user input encrypted_message)
    Returns: All possible decrypted messages based on the 26 shifts. The correct decryption should be a legible message.
    Note: A caesar cipher shift of 26 is the same as a shift of 0 (doesn't change), so shifts 0-25 will be output.
    '''
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Iterate through every possible shift
    for shift in range(len(ALPHABET)):
        decryption = ""
        
        # Iterate through every character in the message you are decrypting
        for character in encrypted_message:
            if character == "o":  # All spaces were represented as "o"s in the encryptions. See encrypt_caesar_cipher()
                decryption += " "
            elif character in ALPHABET:
                num = ALPHABET.find(character)
                num = (num - shift) % 26  # Formula for caesar cipher decryption
                decryption += ALPHABET[num]
            else:
                decryption += character
        print(f"Decryption for Shift = {shift}: {decryption}")

def main():
    # Below is the request for user input of the encrypted message. Comment out to use.
    #encrypted_message = input("Please enter your encrypted message:\n>>> ")
    
    # Below is a pre-determined test encrypted message example with Shift = 3
    # The decrypted message should read "THIS IS A TEST MESSAGE"
    encrypted_message = "WKLVoLVoDoWHVWoPHVVDJH"

    decrypt_caesar_cipher(encrypted_message)
if __name__ == "__main__":
    main()