import functools
from enum import Enum

class HandType(Enum):

    Uninitialised = 0
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7

class Hand:

    cards = ''
    bid_amount = 0
    type = HandType.Uninitialised

    def __init__(self, cards, bid_amount, hand_type):
        self.cards = cards
        self.bid_amount = bid_amount
        self.type = hand_type
        

def get_hand_type(cards):

    card_counts = {}
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    counts = card_counts.values()

    j_count = 0
    if 'J' in card_counts.keys():
        j_count = card_counts['J']

    if len(counts) == 1:
        return HandType.FiveOfAKind
    elif len(counts) == 2:
        if j_count > 0:
            return HandType.FiveOfAKind
        elif 4 in counts:
            return HandType.FourOfAKind
        else:
            return HandType.FullHouse
    elif 3 in counts:
        if j_count > 0:
            return HandType.FourOfAKind
        else:
            return HandType.ThreeOfAKind
    elif len(counts) == 3:
        if j_count == 2:
            return HandType.FourOfAKind
        elif j_count > 0:
            return HandType.FullHouse
        else:
            return HandType.TwoPair
    elif len(counts) == 4:
        if j_count > 0:
            return HandType.ThreeOfAKind
        else:
            return HandType.OnePair
    else:
        if j_count > 0:
            return HandType.OnePair
        else:
            return HandType.HighCard


def get_stronger_card_when_cards_not_the_same(card_a, card_b):

    if card_a == 'A' or card_b == 'A':
        return 'A'
    elif card_a == 'K' or card_b == 'K':
        return 'K'
    elif card_a == 'Q' or card_b == 'Q':
        return 'Q'
    if card_a == 'T' or card_b == 'T':
        return 'T'
    if card_a == '9' or card_b == '9':
        return '9'
    if card_a == '8' or card_b == '8':
        return '8'
    if card_a == '7' or card_b == '7':
        return '7'
    if card_a == '6' or card_b == '6':
        return '6'
    if card_a == '5' or card_b == '5':
        return '5'
    if card_a == '4' or card_b == '4':
        return '4'
    if card_a == '3' or card_b == '3':
        return '3'
    if card_a == '2' or card_b == '2':
        return '2'
    elif card_a == 'J' or card_b == 'J':
        return 'J'
    else:
        return card_a

def get_stronger_cards(first_cards, second_cards):

    for card_index in range(0, len(first_cards)):

        first_card = first_cards[card_index]
        second_card = second_cards[card_index]

        if first_card == second_card:
            continue

        stronger_card = get_stronger_card_when_cards_not_the_same(first_card, second_card)
        if stronger_card == first_card:
            return first_cards
        else:
            return second_cards


def compare_hands(hand_a, hand_b):

    if hand_a.type.value < hand_b.type.value:
        return -1
    elif hand_b.type.value < hand_a.type.value:
        return 1
    
    stronger_cards = get_stronger_cards(hand_a.cards, hand_b.cards)
    if(stronger_cards == hand_a.cards):
        return 1
    else: 
        return -1


def get_hands_sorted_strong_to_weak(hands):

    return sorted(hands, key=functools.cmp_to_key(compare_hands))


def get_hand_from_line(line):

    cards_str, bid_amount_str = line.split()
    return Hand(cards_str, int(bid_amount_str), get_hand_type(cards_str))


def get_hands_from_file(file):

    input_lines = input_file.readlines()
    hands = []
    for line in input_lines:
        hands.append(get_hand_from_line(line))
    return hands


def is_sorted(hands):

    for hand_index in range(0, len(hands) - 1):
        if compare_hands(hands[hand_index], hands[hand_index + 1]) > 0:
            return False
        
    return True


def calculate_total_winnings(file):

    hands = get_hands_from_file(file)
    hands = get_hands_sorted_strong_to_weak(hands)

    for hand in hands:
        print(hand.cards, "\t", hand.type)

    total_winnings = 0

    for hand_index in range(0, len(hands)):

        hand_rank = hand_index + 1
        hand_winnings = hand_rank * hands[hand_index].bid_amount
        total_winnings += hand_winnings
    
    return total_winnings


if __name__ == "__main__":

    input_file = open('input.txt', 'r')

    winnings = calculate_total_winnings(input_file)

    print("The total winnings are:", winnings)