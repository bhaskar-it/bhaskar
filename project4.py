letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in letters:
            position = letters.index(char)
            new_position = (position+shift_key)%26
            cipher_text += letters[new_position]
        else:
            cipher_text += char
    print(f"Here is the text message:{cipher_text}")
def decryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in letters:
            position=letters.index(char)
            new_position =(position - shift_key)%26
            plain_text += letters[new_position]
        else:
            plain_text += char 
    print(f"Here is the message:{cipher_text}")
wann_end=False
while not wann_end:
    what_to_do=input("Type 'encrpty' or 'decrypt':\n")
    text=input("type your message:").lower()
    shift= int(input("enter the shift key:"))
    if what_to_do == 'encrpty':
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do == 'decrypt':
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("type 'yes' to continue, type 'no' to exit:")
    if play_again == 'no':
        wann_end = True
        print("Have a nice day! Bye...........")
            