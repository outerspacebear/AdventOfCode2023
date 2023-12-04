class Number:
    value = 0
    begin_pos_in_line = 0
    end_pos_in_line = 0
    is_part_number = False

    def __init__(self, value, begin_pos, end_pos):
        self.value = value
        self.begin_pos_in_line = begin_pos
        self.end_pos_in_line = end_pos


def get_sum_of_part_numbers(numbers_by_line):

    sum = 0

    for numbers_in_line in numbers_by_line:
        for number in numbers_in_line:
            if number.is_part_number:
                sum += number.value

    return sum


def mark_numbers_adjacent_to_position_as_part_numbers(numbers_by_line, line_index, position):

    if line_index >= 1:
        numbers_in_line_before = numbers_by_line[line_index - 1]
        new_numbers_in_line_before = []

        for number in numbers_in_line_before:
            if position >= number.begin_pos_in_line - 1 and position <= number.end_pos_in_line + 1:
                number.is_part_number = True
            new_numbers_in_line_before.append(number)

        numbers_by_line[line_index - 1] = new_numbers_in_line_before


    numbers_in_line = numbers_by_line[line_index]
    new_numbers_in_line = []
    for number in numbers_in_line:
        if position == number.begin_pos_in_line - 1 or position == number.end_pos_in_line + 1:
            number.is_part_number = True
        new_numbers_in_line.append(number)
    numbers_by_line[line_index] = new_numbers_in_line


    if line_index < len(numbers_by_line) - 1:
        numbers_in_line_after = numbers_by_line[line_index + 1]
        new_numbers_in_line_after = []

        for number in numbers_in_line_after:
            if position >= number.begin_pos_in_line - 1 and position <= number.end_pos_in_line + 1:
                number.is_part_number = True
            new_numbers_in_line_after.append(number)

        numbers_by_line[line_index + 1] = new_numbers_in_line_after

    return numbers_by_line


def mark_numbers_as_part_numbers(numbers_by_line, symbol_positions_by_line):

    line_index = 0

    for symbol_positions_in_line in symbol_positions_by_line:
        for symbol_position in symbol_positions_in_line:
            numbers_by_line = mark_numbers_adjacent_to_position_as_part_numbers(numbers_by_line, line_index, symbol_position)

        line_index += 1

    return numbers_by_line


def get_all_symbol_positions_in_line(line):

    characters = []

    character_position = 0
    for character in line:
        character_position += 1

        if not character.isalnum() and character != "." and not character.isspace():
            characters.append(character_position)

    return characters


def get_all_numbers_in_line(line):

    numbers = []

    current_number_str = ''
    current_number_begin_pos = 0
    character_position = 0

    for character in line:

        character_position += 1

        if character.isdigit():
            if current_number_str == '':
                current_number_begin_pos = character_position
            current_number_str += character
            
        elif current_number_str != '':
            number = Number(int(current_number_str), current_number_begin_pos, character_position - 1)
            numbers.append(number)

            current_number_str = ''

    return numbers



def get_part_numbers_sum(input_file):
    
    numbers_by_line = []
    symbol_positions_by_line = []

    lines = input_file.readlines()
    for line in lines:
        numbers_by_line.append(get_all_numbers_in_line(line))
        symbol_positions_by_line.append(get_all_symbol_positions_in_line(line))

    numbers_by_line = mark_numbers_as_part_numbers(numbers_by_line, symbol_positions_by_line)
    
    return get_sum_of_part_numbers(numbers_by_line)

    #===Debugging
    """
    for test in numbers_by_line:
        print("============================")
        for number in test:
            print("number:", number.value, "\tbeginPos:", number.begin_pos_in_line, "\tendPos:", number.end_pos_in_line)
    print("=======================================\n++++++++++++++++++++++++++++++++++\n=======================================")
    for test in symbol_positions_by_line:
        print("============================")
        for position in test:
            print("symbol position:", position)
    """


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    sum = get_part_numbers_sum(input_file)
    print("The sum of all the part numbers is ", sum)