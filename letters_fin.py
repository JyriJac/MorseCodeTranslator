# 0 = short, 1 = long
def letter(input):
    if input == 'A' or input == 'a':
        return [0,1]
    elif input == 'B' or input == 'b':
        return [1,0,0,0]
    elif input == 'C' or input == 'c':
        return [1,0,1,0]
    elif input == 'D' or input == 'd':
        return [1,0,0]
    elif input == 'E' or input == 'e':
        return [0]
    elif input == 'F' or input == 'f':
        return [0,0,1,0]
    elif input == 'G' or input == 'g':
        return [1,1,0]
    elif input == 'H' or input == 'h':
        return [0,0,0,0]
    elif input == 'I' or input == 'i':
        return [0,0]
    elif input == 'J' or input == 'j':
        return [0,1,1,1]
    elif input == 'K' or input == 'k':
        return [1,0,1]
    elif input == 'L' or input == 'l':
        return [0,1,0,0]
    elif input == 'M' or input == 'm':
        return [1,1]
    elif input == 'N' or input == 'n':
        return [1,0]
    elif input == 'O' or input == 'o':
        return [1,1,1]
    elif input == 'P' or input == 'p':
        return [0,1,1,0]
    elif input == 'Q' or input == 'q':
        return [1,1,0,1]
    elif input == 'R' or input == 'r':
        return [0,1,0]
    elif input == 'S' or input == 's':
        return [0,0,0]
    elif input == 'T' or input == 't':
        return [1]
    elif input == 'U' or input == 'u':
        return [0,0,1]
    elif input == 'V' or input == 'v':
        return [0,0,0,1]
    elif input == 'W' or input == 'w':
        return [0,1,1]
    elif input == 'X' or input == 'x':
        return [1,0,0,1]
    elif input == 'Y' or input == 'y':
        return [1,0,1,1]
    elif input == 'Z' or input == 'z':
        return [1,1,0,0]
    elif input == 'Å' or input == 'å':
        return [0,1,1,0,1]
    elif input == 'Ä' or input == 'ä':
        return [1,0,1,0]
    elif input == 'Ö' or input == 'ö':
        return [1,1,1,0]