import math

def get_minimum_set_for_draw_set(draw_set):

    minimum_set = { "red": 0, "green": 0, "blue": 0}
    
    draws_by_colour = draw_set.split(',')
    for draw in draws_by_colour:
        draw = draw.strip()
        count, colour = draw.split(' ')
        minimum_set[colour] = int(count)

    return minimum_set


def get_game_minimum_set_from_draw_sets(dicts):

    minimum_set = { "red": 0, "green": 0, "blue": 0}

    for dict in dicts:
        for key in dict.keys():
            if dict[key] > minimum_set[key]:
                minimum_set[key] = dict[key]

    return minimum_set


def get_minimum_set_for_game(game_record):

    minimum_sets_for_draws = []

    draw_sets = game_record.split(';')
    for draw_set in draw_sets:
        minimum_sets_for_draws.append(get_minimum_set_for_draw_set(draw_set))
    
    return get_game_minimum_set_from_draw_sets(minimum_sets_for_draws)


def get_minimum_set_power_for_game(game_record):

    minimum_set = get_minimum_set_for_game(game_record)
    minimum_values = minimum_set.values()
    return math.prod(minimum_values)


def get_minimum_sets_powers_sum(input_file):

    minimum_sets_powers = []

    lines = input_file.readlines()
    for line in lines:
        game_record = line.split(':')[1]
        minimum_sets_powers.append(get_minimum_set_power_for_game(game_record))

    return sum(minimum_sets_powers)


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    sum = get_minimum_sets_powers_sum(input_file)
    print("Sum of the powers of the minimum sets for each game: ", sum)
