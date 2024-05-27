def string_to_list(string):
    # Sorts string into list and sorts alphabetically
    string = string.replace("\"", "")
    string = string.split(",")
    string.sort()
    return string


def get_names():
    with open("names.txt") as file:
        names = file.readline()
    names = string_to_list(names)
    return names


def calculate_name_score(pos, name):
    score = 0
    for letter in name:
        score += ord(letter) - 64
    score *= pos
    return score


def main():
    total_score = 0
    names = get_names()
    for index, name in enumerate(names):
        name_score = calculate_name_score(index + 1, name)
        total_score += name_score
    return total_score


print(main())
