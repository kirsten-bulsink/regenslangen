from regenslangen.load import load
from regenslangen.transform import transform
from regenslangen.calculations import get_dice_count_scores
from regenslangen.calculations import get_max_score

# load and transform data
data_raw = load("data.txt")
print(data_raw[0:3])
game = transform(data_raw)
print(game[0:3])

# create a list of the max_score for each round in the game
max_score_all_rounds: list[int] = []
for round in game:
    dicecountscores = get_dice_count_scores(round)
    max_score = get_max_score(dicecountscores)
    max_score_all_rounds.append(max_score)

# sum of max scores is the solution
print(sum(max_score_all_rounds))
