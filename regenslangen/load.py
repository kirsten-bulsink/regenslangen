"""Module containing a function for loading dice input."""


# read the file as a list and split each round
def load(filepath: str) -> list[str]:
    """function that opens a text file and writes every string on a newline to a list item.

    :param filepath: filepath of txt file to load
    """
    with open(filepath, encoding="utf-8") as file:
        file_split = file.read().split("\n\n")
    return file_split
