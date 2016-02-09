class Money(object):

    def __init__(self, cur, value):
        self.cur = cur
        self.value = value

    def show_money(self):
        print('{} dollars.'.format(self.money1))
        print('{} roubles'.format(self.money2))

    def give_money(self, cur, val):
        if cur == 'USD':
            self.money1 -= val
        if cur == 'RUB':
            self.money2 -= val

    def take_money(self, cur, val):
        if cur == 'USD':
            self.money1 += val
        if cur == 'RUB':
            self.money2 += val
