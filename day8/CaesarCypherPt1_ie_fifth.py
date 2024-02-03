from art import logo 

def restart():
     user_input = input("Would you like to restart the program? Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
     if user_input != "yes":
        print("Bye!")
        exit()
     while user_input == "yes":
        main()

def validate_shift(shift):
        if shift > len(alphabet):
            shift = shift % len(alphabet)
        return shift
        
def caesar(text, shift, direction):
        cipher_text = text
        message = ""
        if direction == "decode":
            shift *= -1
        if direction == "encode" or direction == "decode":
                for i in range(len(cipher_text)):
                    if cipher_text[i] not in alphabet:
                        message += str(cipher_text[i])
                    else: 
                        for x in range(len(alphabet)):
                            shifting = shift + x
                            if shifting >= len(alphabet):
                                shifting = (shifting - 26)
                            if cipher_text[i] == alphabet[x]:
                                message += str(alphabet[shifting])
                print(f"Here's the {direction}d result: {message}")
        else:
            print("Error, exiting")
            restart()
            
def main():
    print(logo)
    global alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try: 
        global direction 
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        global text 
        text = input("Type your message:\n").lower()
        global shift 
        shift = int(input("Type the shift number:\n"))
        shift = validate_shift(shift)
    except:
        print("Error, exiting")
        restart()
    caesar(text, shift, direction)
    restart() 

if __name__ == '__main__':
    main()