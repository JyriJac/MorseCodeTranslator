import letters_fin as ltrs
import numbers_fin as nums


def main():
    msg = input("Give message to translate (without special characters.):") #take in message to translate.

    if msg.isalnum(): #check that message contains only letters or numbers.
        for letter in msg: #go trough each letter in message.
            if letter.isalpha():
                check = ltrs.letter(letter)
                for spot in check:
                    if spot == 0:
                        print(spot)
                        #ledi päällä 0.2s
                    else:
                        print(spot)
                        #ledi päällä 0.7s
            else:
                check = nums.numbers(int(letter))
                for spot in check:
                    if spot == 0:     
                        print(spot)
                        #ledi päällä 0.2s
                    else:
                        print(spot)
                        #ledi päällä 0.7s


if __name__ == "__main__":
    main()
