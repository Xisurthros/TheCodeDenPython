def listStoringLast():
    item = {}
    x = 0
    while True:
        listVariable = input().upper()
        item[listVariable] = x
        x += 1
        print(item)


class CoinPurse:
    def __init__(self, name):
        self.name = name
        self.userCoinAmount = 0

    def add_coin(self, value):
        self.userCoinAmount += value

    def print_information(self):
        print(self.name)
        print(self.userCoinAmount)
