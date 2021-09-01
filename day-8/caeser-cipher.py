alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(dir, encode_txt, shift_num):
    cipher_text = ''
    for letter in encode_txt:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_num if dir == "encode" else position - shift_num
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {dir} text is {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caeser(direction, text, shift)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == 'no':
        should_continue = False
        print("GoodBye")


