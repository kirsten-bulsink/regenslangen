# Regenslangen
![Continuous Integration build in GitHub Actions](https://github.com/<your_github_username>/python-intermediate-inflammation/actions/workflows/main.yml/badge.svg?branch=main)

Regenslangen is a software program that calculates a maximum score in the dice game Regenslangen.

## Explanation of the Regenslangen game
The regenslangen game is inspired by Advent of Code puzzles and the game 'regenwormen'. It was invented by Vince van Noort as my 'surprise' for 'Sinterklaas'. 

The goal: find the maximum score in each round. The maximun score of all rounds togehter returns the code that opens my present!! :smile:

The rules:
- Dice have the possible outcomes of 1 till 5 or a Python (regenslang). The value of a dice is the same as the dice number and Pythons have a value of 5.
- There are 8 dice in the game. Therefore, you can maximally take 8 dice per round.
- If you choose a dice number (1 till 5 or P), you need to take all dice of that number (or all Pythons).
- If a dice number (1 till 5 or P) is chosen in a certain round, it cannot be chosen anymore in the next tosses.
- The total set of chosen dice should always include a Python to be valid.


## Prerequisites
Regenslangen does not require any additional Python packages to run.

The following optional packages are required to run Regenslangen unit tests:
- [pytest](https://docs.pytest.org/en/stable/) - Regenslangen unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

