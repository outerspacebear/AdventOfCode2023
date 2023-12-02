Max_Cubes_By_Colour = { "red": 12, "green": 13, "blue": 14}

def is_draw_possible(draw):

    draw = draw.strip()
    count, colour = draw.split(' ')

    return int(count) <= Max_Cubes_By_Colour[colour]

def is_draw_set_possible(draw_set):

    draws_by_colour = draw_set.split(',')
    for draw in draws_by_colour:
        if not is_draw_possible(draw):
            return False
        
    return True

def is_game_possible(game_record):
    
    draw_sets = game_record.split(';')
    for draw_set in draw_sets:
        if not is_draw_set_possible(draw_set):
            return False
        
    return True

def get_game_id(game_id_str):
    
    game_id = game_id_str.split(' ')[1]
    return int(game_id)

def get_possible_game_ids_sum(input_file):

    possible_game_ids = []

    lines = input_file.readlines()
    for line in lines:
        game_id_string, game_record = line.split(':')
        game_id = get_game_id(game_id_string)
        if is_game_possible(game_record):
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    sum = get_possible_game_ids_sum(input_file)
    print("Sum: ", sum)
