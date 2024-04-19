"""Module containing functions that calculate scores of different dice choices in a game."""

from collections import Counter
import random


def get_dice_count_scores(game_round: list[str]) -> list[tuple[int, str, int, int]]:
    """
    For a game round (list) with multiple tosses (strings), determine each possible choice of dice
    and the matching score of this choice (tuple: toss_nr, dice, count, score).

    :param round: list of tosses (strings) that represent one round in the game
    """

    round_scores = []
    toss_nr = 1
    for toss in game_round:
        toss_counts = Counter(toss)
        for dice, count in toss_counts.items():
            score = int(dice) * count if dice != "P" else 5 * count
            tup_dicecountscore = (toss_nr, dice, count, score)
            round_scores.append(tup_dicecountscore)
        toss_nr += 1
    return round_scores


def get_a_valid_score(
    dicecountscores: list[tuple[int, str, int, int]],
) -> tuple[int, bool]:
    """
    Randomly chooses a dice from each toss in a round until maximum number of dice (8)
    is reached or until there is no valid option left to choose from. Sums the score of this 'try'.

    Two other game rules are checked to create a valid score:
    - if a dice number (1 till 5 or P) is used, it cannot be chosen anymore in the next tosses.
    - the total set of chosen dice should include a Python.

    :param dicecountscores: list of tuples with each possible choice of dice (toss_nr, dice, count, score)
    """

    total_dice_used = 0
    total_score = 0
    diff_dice_used = []
    toss_nr = 1
    while total_dice_used < 9:
        print(f" round {toss_nr}")
        toss_subset = [i for i in dicecountscores if i[0] == toss_nr]
        # remove the options that are not possible because of the dice choices beforehand
        toss_subset_legal = [i for i in toss_subset if i[1] not in diff_dice_used]

        # check if there is any legal option left
        if toss_subset_legal == []:
            print("sample is empty, impossible")
            break
        # if so, choose a random option
        choice = random.choice(toss_subset_legal)
        (toss_nr, dice, count, score) = choice

        # check the amount of dice used
        total_dice_used += count
        if total_dice_used > 8:
            print(
                f" this choice would use {total_dice_used} dice, which is impossible. keep the latest total score: {total_score}"
            )
            break

        # calculate the score and add the chosen dice to the list of diff_dice_used
        total_score += score
        diff_dice_used.append(dice)
        print(f" diff dice used {diff_dice_used}")
        print(f" total dice used is {total_dice_used}")
        print(f" total score until now is {total_score}")
        toss_nr += 1
    print("stop")
    # add a logical that indicates whether a Python was used (which is obligated)
    with_python = "P" in diff_dice_used
    return total_score, with_python


def get_max_score(dicecountscores: list[tuple[int, str, int, int]]) -> int:
    """
    Get a valid score a 1000 times, then take the max score.

    :param dicecountscores: list of tuples with each possible choice of dice (toss_nr, dice, count, score)
    """

    all_scores = []
    for _ in range(1000):
        score = get_a_valid_score(dicecountscores)
        number, python = score
        # only add to score list if python is true
        if python:
            all_scores.append(number)
    max_score = max(all_scores)
    return max_score
