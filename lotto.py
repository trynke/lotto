import keyboard
import random

def get_barrel():
    print("Pressed enter")


def get_number_of_barrels():
    N = str(input('Enter the number of barrels. It must be an integer greater than 0 \n'))
    if N.isdigit() and int(N) > 0:
        return int(N)
    else:
        print("You entered an incorrect value. Let's try again")
        return get_number_of_barrels()


def main():
    print("Random numbers generation (as in lotto game) \n")
    N = get_number_of_barrels()
    barrels = [i for i in range(1, N+1)]


    keyboard.add_hotkey('Enter', get_barrel)
    keyboard.wait('Esc')


if __name__ == '__main__':
    main()