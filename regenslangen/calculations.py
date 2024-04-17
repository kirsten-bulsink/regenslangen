from collections import Counter
import random


# fun that returns tuples of (worp_nr, dice, count, score) for each worp in ronde
def get_dice_count_scores(ronde: list[str]) -> list[tuple[int, str, int, int]]:
    ronde_scores = []
    worp_nr = 1
    for worp in ronde:
        worp_counts = Counter(worp)
        for dice, count in worp_counts.items():
            score = int(dice) * count if dice != "P" else 5 * count
            tup_dicecountscore = (worp_nr, dice, count, score)
            ronde_scores.append(tup_dicecountscore)
        worp_nr += 1
    return ronde_scores


# fun that randomly chooses one 'legal' option from each worp in a round until maximum number of dice (8) is reached or
# there is no valid option left to choose from
def get_a_valid_score(
    dicecountscores: list[tuple[int, str, int, int]],
) -> tuple[int, bool]:
    total_dice_used = 0
    total_score = 0
    diff_dice_used = []
    worp_nr = 1
    while total_dice_used < 9:
        print(f" round {worp_nr}")
        worp_subset = [i for i in dicecountscores if i[0] == worp_nr]
        # remove the options that are not possible because of the dice choices beforehand
        worp_subset_legal = [i for i in worp_subset if i[1] not in diff_dice_used]

        # check if there is any legal option left
        if worp_subset_legal == []:
            print("sample is empty, impossible")
            break
        # if so, choose a random option
        choice = random.choice(worp_subset_legal)
        (worp_nr, dice, count, score) = choice

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
        worp_nr += 1
    print("stop")
    # add a logical that indicates whether a Python was used (which is obligated)
    with_python = "P" in diff_dice_used
    return total_score, with_python


# get a valid score a 1000 times, then take the max score
def get_max_score(dicecountscores: list[tuple[int, str, int, int]]) -> int:
    all_scores = []
    for i in range(1000):
        score = get_a_valid_score(dicecountscores)
        number, python = score
        # only add to score list if python is true
        if python:
            all_scores.append(number)
    max_score = max(all_scores)
    return max_score
