from modules.testing import *


def main():
    name = input("Enter your name: ")
    purse = CoinPurse(name)
    while True:
        value = int(input('Enter coin value (cents): '))
        if value <= 0:
            break
        purse.add_coin(value)
    purse.print_information()


if __name__ == '__main__':
    main()
