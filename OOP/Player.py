import Money
import Session


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