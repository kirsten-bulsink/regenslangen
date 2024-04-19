"""Module containing functions for transforming the dice input."""


def transform(data: list[str]) -> list[list[str]]:
    """Transform list of each round to a nested list 'game' of each toss in each round.

    :param data: list of strings that represent rounds in the dice game
    """
    game = []
    for game_round in data:
        tosses = game_round.splitlines()
        # remove the round name
        game.append(tosses[1:])
    return game
