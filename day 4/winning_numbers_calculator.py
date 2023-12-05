
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

    print(won_numbers_count, points)
    return points


def get_points_from_scratchcard(card):

    all_numbers = card.split(':')[1]
    winning_numbers_text, present_numbers_text = all_numbers.split('|')
    winning_numbers = get_numbers_from_text(winning_numbers_text)
    present_numbers = get_numbers_from_text(present_numbers_text)
    matching_numbers = [present_number for present_number in present_numbers if present_number in winning_numbers]
    matching_numbers_count = len(matching_numbers)

    return get_points(matching_numbers_count)


def get_points_from_scratchcards(file):
    
    points_total = 0
    
    cards = input_file.readlines()
    for card in cards:
        points_total += get_points_from_scratchcard(card)

    return points_total

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    points = get_points_from_scratchcards(input_file)
    print("The total points from all scratchcards are:", points)