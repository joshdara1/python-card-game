import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from card_game import Card, Deck, Game, Player


class CardGameTests(unittest.TestCase):
    def test_deck_contains_every_card_once(self):
        deck = Deck()
        self.assertEqual({(c.value, c.suit) for c in deck.cards},
                         {(v, s) for v in range(2, 15) for s in range(4)})
        self.assertEqual(len(deck.cards), 52)

    def test_dealing_exhausts_deck_without_repeats(self):
        deck = Deck()
        dealt = [deck.rm_card() for _ in range(52)]
        self.assertEqual(len({(c.value, c.suit) for c in dealt}), 52)
        self.assertIsNone(deck.rm_card())

    def test_rank_takes_priority_over_suit(self):
        self.assertGreater(Card(14, 0), Card(13, 3))
        self.assertLess(Card(2, 3), Card(3, 0))

    def test_equal_ranks_are_ordered_by_suit(self):
        self.assertGreater(Card(10, 3), Card(10, 0))
        self.assertLess(Card(10, 0), Card(10, 3))

    def test_card_label(self):
        self.assertEqual(repr(Card(14, 0)), 'Ace of Spades')

    def test_score_and_winner(self):
        first, second = Player('Josh'), Player('Alex')
        self.assertIsNone(Game.winner(None, first, second))
        first.update_score()
        self.assertEqual(Game.winner(None, first, second), 'Josh')
        second.update_score()
        second.update_score()
        self.assertEqual(Game.winner(None, first, second), 'Alex')

    def test_blank_name_is_rejected(self):
        with patch('builtins.input', side_effect=['  ', ' Josh ']), redirect_stdout(io.StringIO()):
            self.assertEqual(Game.get_player_name(None, 'Player 1'), 'Josh')

    def test_full_game_awards_exactly_26_points(self):
        with patch('builtins.input', side_effect=['Josh', 'Alex'] + [''] * 26), redirect_stdout(io.StringIO()):
            game = Game()
            game.play_game()
        self.assertEqual(game.p1.score + game.p2.score, 26)
        self.assertEqual(len(game.deck.cards), 0)

    def test_quitting_before_first_round_reports_tie(self):
        output = io.StringIO()
        with patch('builtins.input', side_effect=['Josh', 'Alex', ' Q ']), redirect_stdout(output):
            game = Game()
            game.play_game()
        self.assertIn('The game is over. It was a tie!', output.getvalue())
        self.assertEqual(len(game.deck.cards), 52)


if __name__ == '__main__':
    unittest.main()
