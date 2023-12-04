class Number:
    value = 0
    begin_pos_in_line = 0
    end_pos_in_line = 0
    is_part_number = False

    def __init__(self, value, begin_pos, end_pos):
        self.value = value
        self.begin_pos_in_line = begin_pos
        self.end_pos_in_line = end_pos

class Symbol:
    symbol = ''
    position = 0

    def __init__(self, symbol, pos):
        self.symbol = symbol
        self.position = pos


def get_sum_of_part_numbers(numbers_by_line):

    sum = 0

    for numbers_in_line in numbers_by_line:
        for number in numbers_in_line:
            if number.is_part_number:
                sum += number.value

    return sum


def mark_numbers_adjacent_to_position_as_part_numbers(numbers_by_line, line_index, symbol):

    adjacent_numbers = []

    if line_index >= 1:
        numbers_in_line_before = numbers_by_line[line_index - 1]
        new_numbers_in_line_before = []

        for number in numbers_in_line_before:
            if symbol.position >= number.begin_pos_in_line - 1 and symbol.position <= number.end_pos_in_line + 1:
                number.is_part_number = True
                adjacent_numbers.append(number.value)
            new_numbers_in_line_before.append(number)

        numbers_by_line[line_index - 1] = new_numbers_in_line_before


    numbers_in_line = numbers_by_line[line_index]
    new_numbers_in_line = []
    for number in numbers_in_line:
        if symbol.position == number.begin_pos_in_line - 1 or symbol.position == number.end_pos_in_line + 1:
            number.is_part_number = True
            adjacent_numbers.append(number.value)
        new_numbers_in_line.append(number)
    numbers_by_line[line_index] = new_numbers_in_line


    if line_index < len(numbers_by_line) - 1:
        numbers_in_line_after = numbers_by_line[line_index + 1]
        new_numbers_in_line_after = []

        for number in numbers_in_line_after:
            if symbol.position >= number.begin_pos_in_line - 1 and symbol.position <= number.end_pos_in_line + 1:
                number.is_part_number = True
                adjacent_numbers.append(number.value)
            new_numbers_in_line_after.append(number)

        numbers_by_line[line_index + 1] = new_numbers_in_line_after


    gear_ratio = 0
    if symbol.symbol == '*' and len(adjacent_numbers) == 2:
        gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]

    return numbers_by_line, gear_ratio


def mark_numbers_as_part_numbers(numbers_by_line, symbols_by_line):

    line_index = 0
    gear_ratio_sum = 0

    for symbols_in_line in symbols_by_line:
        for symbol in symbols_in_line:
            numbers_by_line, gear_ratio = mark_numbers_adjacent_to_position_as_part_numbers(numbers_by_line, line_index, symbol)
            gear_ratio_sum += gear_ratio

        line_index += 1

    return numbers_by_line, gear_ratio_sum


def get_all_symbol_positions_in_line(line):

    symbols = []

    symbol_position = 0
    for character in line:
        symbol_position += 1

        if not character.isalnum() and character != "." and not character.isspace():
            symbols.append(Symbol(character, symbol_position))

    return symbols


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
    symbols_by_line = []

    lines = input_file.readlines()
    for line in lines:
        numbers_by_line.append(get_all_numbers_in_line(line))
        symbols_by_line.append(get_all_symbol_positions_in_line(line))

    numbers_by_line, gear_ratio_sum = mark_numbers_as_part_numbers(numbers_by_line, symbols_by_line)
    
    return get_sum_of_part_numbers(numbers_by_line), gear_ratio_sum

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
    sum, gear_ratio_sum = get_part_numbers_sum(input_file)
    print("The sum of all the part numbers is ", sum)
    print("The sum of all the gear ratios is ", gear_ratio_sum)