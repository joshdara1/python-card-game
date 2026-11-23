from random import shuffle

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def update_score(self):
        self.score += 1


class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(self.get_player_name("Player 1"))
        self.p2 = Player(self.get_player_name("Player 2"))

    def get_player_name(self, player_number):
        name = input(f"{player_number} name: ")
        while not name.strip():  # Validate non-empty input
            print("Please enter a valid name.")
            name = input(f"{player_number} name: ")
        return name.strip()

    def display_scores_interface(self):
        print("\n====================")
        print(f"Scores - {self.p1.name}: {self.p1.score}  |  {self.p2.name}: {self.p2.score}")
        print("====================\n")

    def display_cards(self, player1, card1, player2, card2):
        print(f"{player1.name} drew {card1}  |  {player2.name} drew {card2}")

    def display_winner(self, winner):
        print(f"{winner} is the winner this round")

    def play_game(self):
        cards = self.deck.cards
        print("Let the game begin!")
        while len(cards) >= 2:
            response = input("Press any key to play or 'q' to quit: ")
            if response.strip().lower() == 'q':
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()

            self.display_cards(self.p1, p1c, self.p2, p2c)

            if p1c > p2c:
                self.p1.update_score()
                self.display_winner(self.p1.name)
            else:
                self.p2.update_score()
                self.display_winner(self.p2.name)

            self.display_scores_interface()

        win = self.winner(self.p1, self.p2)
        if win is None:
            print("The game is over. It was a tie!")
        else:
            print(f"The game is over. {win} wins!")

    def winner(self, p1, p2):
        if p1.score > p2.score:
            return p1.name
        if p1.score < p2.score:
            return p2.name
        return None

if __name__ == "__main__":
    game = Game()
    game.play_game()
