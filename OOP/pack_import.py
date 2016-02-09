
import Money
import Player
import Session





if __name__ == '__main__':
    p = Player('name', 'log', 'email', 'pass')
    p.show_money()
    p.take_money('USD', 250)
    p.show_money()
