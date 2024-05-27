from statistics import *


def get_card_value(card):
    try:
        return int(card)
    except ValueError:
        if card == "T":
            return 10
        elif card == "J":
            return 11
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        return 14  # Ace


def get_suits(hand):
    return [card[1] for card in hand]


def get_values(hand):
    return [get_card_value(card[0]) for card in hand]


def is_flush(hand):
    return get_suits(hand).count(get_suits(hand)[0]) == 5


def is_straight(hand):
    values = get_values(hand)
    values.sort()

    start = values[0]
    check = [x for x in range(start, start + 5)]

    return check == values


def is_n_of_kind_v(hand, n, v):
    count = 0
    values = get_values(hand)
    for value in values:
        if value == v:
            count += 1
    return n == count


def calculate_score(hand):
    """
    :param hand: Cards in players hand
    :return score: Integer deciding players hand
    0 - Straight Flush
    1 - Four of a Kind
    3 - Full House
    4 - Flush
    5 - Straight
    6 - Three of a kind
    7 - Two Pair
    8 - Pair
    9 - High Card
    """

    if is_flush(hand) and is_straight(hand):
        # Straight flush
        return 0
    elif is_flush(hand):
        #  Regular Flush
        return 4
    elif is_straight(hand):
        # Regular Straight
        return 5

    if len(set(get_values(hand))) == 2:
        # 4 of a kind OR Full house
        for number in get_values(hand):
            if is_n_of_kind_v(hand, 4, number):
                # 4 of a kind
                return 1
            # Full house
            return 3
    if len(set(get_values(hand))) == 3:
        # 3 of a kind OR Two pair
        for number in get_values(hand):
            if is_n_of_kind_v(hand, 3, number):
                # 3 of a kind
                return 6
            # Two pair
            return 7

    for number in get_values(hand):
        if is_n_of_kind_v(hand, 2, number):
            # Pair
            return 8
    return 9


def split_hands(line):
    hands = []

    card = ""
    hand = []
    count = 0
    for character in line:
        if character == " ":
            continue
        card += character
        count += 1

        if count % 2 == 0:
            hand.append(card)
            card = ""
        if len(hand) == 5:
            hands.append(hand)
            hand = []
    return hands


def remove_pair(values):
    return list(filter((mode(values)).__ne__, values))


def settle_draw(player1_hand, player2_hand, score):
    player1_hand = sorted(get_values(player1_hand))
    player1_hand.reverse()

    player2_hand = sorted(get_values(player2_hand))
    player2_hand.reverse()

    if score in [8, 7, 6]:
        # Check who has higher value pair/trio
        if score == 8 or score == 6:
            if mode(player1_hand) > mode(player2_hand):
                return True
            elif mode(player1_hand) < mode(player2_hand):
                return False
        if score == 7:
            player1_duplicates = []
            player2_duplicates = []
            for number in player1_hand:
                if player1_hand.count(number) == 2 and number not in player1_duplicates:
                    player1_duplicates.append(number)
            for number in player2_hand:
                if player2_hand.count(number) == 2 and number not in player2_duplicates:
                    player2_duplicates.append(number)
            for i in range(2):
                if player1_duplicates[i] > player2_duplicates[i]:
                    return True
                elif player1_duplicates[i] < player2_duplicates[i]:
                    return False
        # Remove Pair from hand - if duplicates are same
        player1_hand = remove_pair(player1_hand)
        player2_hand = remove_pair(player2_hand)

        if score == 7:
            # Remove second pair
            player1_hand = remove_pair(player1_hand)
            player2_hand = remove_pair(player2_hand)

    for i in range(len(player1_hand)):
        if player2_hand[i] == player1_hand[i]:
            continue
        if player2_hand[i] > player1_hand[i]:
            return False
        return True


def main():
    win_count = 0
    with open("poker.txt") as file:
        for _ in range(1000):
            game = file.readline()
            hands = split_hands(game)
            player1_score = calculate_score(hands[0])
            player2_score = calculate_score(hands[1])

            if player1_score < player2_score:
                win_count += 1
                continue
            elif player1_score == player2_score:
                win_count += settle_draw(hands[0], hands[1], player1_score)
    return win_count


print(main())
