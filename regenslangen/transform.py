# create a nested list 'game' with a list of 'worpen' in each 'round'
def transform(data: list[str]) -> list[list[str]]:
    game = []
    for round in data:
        worpen = round.splitlines()
        # remove the round name
        game.append(worpen[1:])
    return game
