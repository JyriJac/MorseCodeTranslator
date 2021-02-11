import letters_fin as ltrs
import numbers_fin as nums


def main():
    msg = input("Give message to translate (without special characters.):")

    if msg.isalnum():
        for letter in msg:
            print(letter)


if __name__ == "__main__":
    main()
