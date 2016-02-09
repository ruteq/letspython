import datetime


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


class Session(object):
    def new_session(self):
        def __enter__(self):
                start = datetime.datetime.now()
        def __exit__(self, exc_type, exc_val, exc_tb):
            finish = datetime.datetime.now()
        total = (finish - start)

class Player(Money, Session):

    def __init__(self, player_name, login, email, password):
        self.name = player_name
        self.login = login
        self.email = email
        self.password = password

        self.health = 100
        self.experience = 0

        self.money1 = 0
        self.money2 = 0

        self.session = {}
        self.last_session = 0



if __name__ == '__main__':
    p = Player('name', 'log', 'email', 'pass')
    p.show_money()
    p.take_money('USD', 250)
    p.show_money()



