import keyboard
import random

def get_barrel():
    print("Pressed enter")


def main():
    keyboard.add_hotkey('Enter', get_barrel)
    keyboard.wait('Esc')


if __name__ == '__main__':
    main()