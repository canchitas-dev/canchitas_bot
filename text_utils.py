import silabeador


def normalize(line):
    line = list(line)

    if len(line) != 0 and line[0] == "y" and line[1] == " ":
        line[0] = "a"

    line = "".join(line)
    return line


def is_haiku(string):
    '''Is our string ES haiku?'''
    string = string.split("\n")

    if len(string) != 3:
        return False

    string = [normalize(line) for line in string]
    string = [silabeador.syllabify(line) for line in string]

    return len(string[0]) == 5 and len(string[1]) == 7 and len(string[2]) == 5
