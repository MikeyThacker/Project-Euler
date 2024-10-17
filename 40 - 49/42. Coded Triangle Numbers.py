def get_words():
    with open("words.txt") as file:
        words = file.readline()
    words = words.replace("\"", "")
    words = words.split(",")
    return words


def calculate_score(word):
    score = 0
    for letter in word:
        score += ord(letter) - 64
    return score


def get_triangle_number(n):
    return 0.5 * n * (n + 1)


def check_score(score, triangle_numbers):
    if score in triangle_numbers:
        return True
    return False


def main():
    triangle_numbers = set([1, 3, 6, 10, 15, 21, 28, 36, 45])
    triangle_word_count = 0

    words = get_words()
    for word in words:
        score = calculate_score(word)
        if check_score(score, triangle_numbers):
            triangle_word_count += 1

        elif score > max(triangle_numbers):
            while max(triangle_numbers) < score:
                triangle_numbers.add(get_triangle_number(len(triangle_numbers) + 1))
            if check_score(score, triangle_numbers):
                triangle_word_count += 1

    return triangle_word_count


print(main())
