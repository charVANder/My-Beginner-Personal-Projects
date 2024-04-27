'''
Evangeline Kim
Oct. 22nd, 2023
Code to take any message and encrypt the Caesar Cipher code for a given shift (25 possible)
'''

def encrypt_caesar_cipher(message, shift):
    '''Function encrypt_caesar_cipher takes a message and outputs a caesar cipher encryption based on a chosen shift.
    Parameters: The message to be encrypted (message), and the shift the user wants (shift)--25 possible.
    Note: Only 25 shifts are possible because a shift of 0 or 26 will result in the same message.
    Returns: The new caesar cipher encrypted message.
    '''
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryption = ""
    
    # Iterate through all character positions in the message
    for characters in range(len(message)):
        character = message[characters]
        if character == " ":  # Replace all spaces w/ "o" --> HELLOoWORLD
            encryption += "o"
        elif character in ALPHABET:
            num = ALPHABET.find(character)
            num = (num + shift) % 26  # Formula for caesar cipher encryption
            encryption += ALPHABET[num]
        else:
            encryption += character  # Other characters such as ! or # will stay the same
    print(f"Caesar Cipher Encryption for Shift = {shift}: {encryption}")
        
def main():
    # Ask for message to encrypt from the user. Comment out line below for use.
    #message = input("Please enter the message to be encrypted:\n>>> ").upper()
    
    # Account for multple user input errors when requesting shift
    while True:
        try:
            shift = int(input("Please enter the shift for your Caesar Cipher (input an integer from 1-25):\n>>> "))
        except ValueError or shift < 1 or shift > 25:
            print("Invalid input. Please try again.")
        else:
            break 

    # Below is a pre-determined test message to run encrypt_caesar_cipher().
    # For a Shift = 3, the output should be "WKLVoLVoDoWHVWoPHVVDJH"
    message = "THIS IS A TEST MESSAGE"

    encrypt_caesar_cipher(message, shift)

if __name__ == "__main__":
    main()