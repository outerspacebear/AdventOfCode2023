
class ScratchCard:
    card = ''
    copies = 1

    def __init__(self, card_text):
        self.card = card_text

def get_numbers_from_text(text):

    numbers_text = text.split()
    
    numbers = [int(number_text) for number_text in numbers_text]

    return numbers

def get_points(won_numbers_count):

    points = 0

    for x in range(0, won_numbers_count):
        if points == 0:
            points = 1
        else:
            points = points * 2

    return points


def get_points_and_matching_numbers_count_from_scratchcard(card):

    all_numbers = card.split(':')[1]
    winning_numbers_text, present_numbers_text = all_numbers.split('|')
    winning_numbers = get_numbers_from_text(winning_numbers_text)
    present_numbers = get_numbers_from_text(present_numbers_text)
    matching_numbers = [present_number for present_number in present_numbers if present_number in winning_numbers]
    matching_numbers_count = len(matching_numbers)

    return get_points(matching_numbers_count), matching_numbers_count


def get_number_of_copies(cards):

    copies = 0

    for card in cards:
        copies += card.copies

    return copies


def get_points_and_number_of_copies_from_scratchcards(file):
    
    points_total = 0
    
    input_lines = input_file.readlines()
    cards = []

    for line in input_lines:
        cards.append(ScratchCard(line))

    for card_index in range(0, len(cards)):
        points, matching_numbers_count = get_points_and_matching_numbers_count_from_scratchcard(cards[card_index].card)
        points_total += points

        print("card index", card_index, "matches", matching_numbers_count, "copies", cards[card_index].copies)
        for copy_index_adder in range(1, matching_numbers_count + 1):
            copy_index = card_index + copy_index_adder

            if copy_index < len(cards):
                cards[copy_index].copies += cards[card_index].copies
                print("\t\tc index", copy_index, "copies", cards[copy_index].copies)
       


    return points_total, get_number_of_copies(cards)

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    points, num_copies = get_points_and_number_of_copies_from_scratchcards(input_file)
    print("The total points from all scratchcards are:", points)
    print("The total numbers of copies of each card are:", num_copies)