def get_calbration_value_for_line(line):
    
    first_digit = "-1"
    last_digit = "-1"
    
    for character in line:
        if character.isdigit():
            if first_digit == "-1":
                first_digit = character
            last_digit = character
    
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
    
