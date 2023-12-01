def try_get_digit_from_string(string):
    if string.endswith('one'):
        return '1'
    elif string.endswith('two'):
        return '2'
    elif string.endswith('three'):
        return '3'
    elif string.endswith('four'):
        return '4'
    elif string.endswith('five'):
        return '5'
    elif string.endswith('six'):
        return '6'
    elif string.endswith('seven'):
        return '7'
    elif string.endswith('eight'):
        return '8'
    elif string.endswith('nine'):
        return '9'
    else:
        return None

def get_digits_in_line_as_strs(line):

    digits_in_line = []
    current_unevaluated_string = ''

    for character in line:
        if character.isdigit():
            digits_in_line.append(character)
            current_unevaluated_string = ''
        else:
            current_unevaluated_string += character
            digit_from_string = try_get_digit_from_string(current_unevaluated_string)
            if digit_from_string != None:
                digits_in_line.append(digit_from_string)

    return digits_in_line


def get_calbration_value_for_line(line):
    
    digits_in_line = get_digits_in_line_as_strs(line)
    print(digits_in_line)
    first_digit = digits_in_line[0]
    last_digit = digits_in_line[-1]
    
    return first_digit + last_digit


def get_calibration_values_sums(input_file):

    calbration_values_sum = 0

    lines = input_file.readlines()
    for line in lines:
        calibration_value = int(get_calbration_value_for_line(line))
        calbration_values_sum += calibration_value

    return calbration_values_sum

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    sum = get_calibration_values_sums(input_file)
    print("Sum: ", sum)
    
