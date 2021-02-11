import letters_fin as ltrs
import numbers_fin as nums


def main():
    msg_raw = input("Give message to translate (without special characters.):") #take in message to translate.
    msg = msg_raw.replace(" ", "")
    if msg.isalnum(): #check that message contains only letters or numbers.
        for letter in msg: #go trough each letter in message.
            if letter.isalpha(): #check whether letter is alphabet or number
                check = ltrs.letter(letter) #check matching morse code for letter
                for spot in check:
                    if spot == 0:
                        print(spot) #led on 0.2s
                    else:
                        print(spot) #led off 0.7s
            else:
                check = nums.numbers(int(letter)) #check matching morse code for number
                for spot in check:
                    if spot == 0:     
                        print(spot) #led on 0.2s
                    else:
                        print(spot) #led off 0.7s                     


if __name__ == "__main__":
    main()
