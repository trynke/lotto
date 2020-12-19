import keyboard
import random

def get_barrel(barrels):
    if len(barrels) != 0:
        rand = random.choice(barrels)
        print(rand)
        barrels.remove(rand)
    else:
        print("There aren't any barrels left. Press Esc to close the program, goodbye!")


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
    barrels = [[i for i in range(1, N+1)]]
    print("Now press Space to get one random barrel, or press Esc to exit")
    keyboard.add_hotkey('space', get_barrel, args=barrels)
    keyboard.wait('Esc')


if __name__ == '__main__':
    main()