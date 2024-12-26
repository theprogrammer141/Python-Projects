from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_amount, input_direction):
    if input_direction == "encode":
        cipher_text = ""
        for letter in input_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % len(alphabet)
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(cipher_text)
    elif input_direction == "decode":
        plain_text = ""
        for letter in input_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift_amount) % len(alphabet)
                new_letter = alphabet[new_position]
                plain_text += new_letter
            else:
                plain_text += letter
        print(plain_text)

caesar(text, shift, direction)

while True:
    repeat = str(input("Do you want to repeat again? Type \'yes\' to repeat and \'no\' to exit:"))
    if repeat == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    elif repeat == "no":
        print("Goodbye")
        break

