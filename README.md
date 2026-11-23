# Python Card Game

A small command-line card game originally developed for first-year university coursework in 2023. It demonstrates Python classes, object comparisons, shuffled decks, input validation and score tracking.

## Run

Requires Python 3. No additional packages are needed.

```sh
python3 card_game.py
```

Enter two player names. Press Enter to draw a card for each player, or enter `q` to stop. A complete game has 26 rounds. The higher-ranked card earns one point; equal ranks are resolved by suit in the implementation's order: Clubs > Diamonds > Hearts > Spades. The player with the highest score wins.

This is a local two-player game of chance. There is no AI opponent, graphical interface or saved leaderboard. Entering “robot” simply names a player; it does not enable another mode.

## Design

- `Card`: stores rank and suit, displays card names and implements comparisons.
- `Deck`: creates and shuffles 52 unique cards, then deals without replacement.
- `Player`: stores a name and score.
- `Game`: handles input, rounds, score display and the final result.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

Tests cover deck contents and exhaustion, rank and suit comparisons, labels, score and winner calculation, blank-name validation, a full game and early quitting.

## Project history

The original coursework is preserved in the university repository. This portfolio edition was prepared with AI assistance after graduation: it removes duplicate score state, improves tie messages and whitespace handling, adds an import guard, and introduces automated tests and this README. These later improvements are separate from the original submitted coursework.

Possible future improvements include separating game logic from console input and adding a replay option.
