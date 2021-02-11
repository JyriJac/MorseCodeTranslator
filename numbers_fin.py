# 0 = short, 1 = long
def numbers(input):
    if input == 1:
        return [1,0,0,0,0]
    elif input == 2:
        return [1,1,0,0,0]
    elif input == 3:
        return [1,1,1,0,0]
    elif input == 4:
        return [1,1,1,1,0]
    elif input == 5:
        return[1,1,1,1,1]
    elif input == 6:
        return [0,1,1,1,1]
    elif input == 7:
        return [0,0,1,1,1]
    elif input == 8:
        return [0,0,0,1,1]
    elif input == 9:
        return [0,0,0,0,1]
    elif input == 0:
        return [0,0,0,0,0]