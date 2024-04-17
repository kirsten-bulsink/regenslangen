# read the file as a list and split each round
def load(path: str) -> list[str]:
    file = open(path)
    file_split = file.read().split("\n\n")
    return file_split
