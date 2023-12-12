import math



def get_distance_travelled_by_holding_down_for_time(hold_down_time, total_time):

    speed = hold_down_time
    travel_time = total_time - hold_down_time
    distance = speed * travel_time
    return distance


def get_number_of_ways_to_win_race(race_time, race_record_distance):

    number_of_ways_to_win = 0

    for hold_down_time in range(0, race_time + 1):
        if get_distance_travelled_by_holding_down_for_time(hold_down_time, race_time) > race_record_distance:
            number_of_ways_to_win += 1

    return number_of_ways_to_win


def get_number_from_line(line):

    strs = line.split()
    number_str = ''
    for str in strs:
        number_str += str
    return int(number_str)


def get_number_of_ways_to_win_main_race(input_file):

    input_lines = input_file.readlines()
    race_times_str = input_lines[0].split(':')[1]
    race_distances_str = input_lines[1].split(':')[1]

    race_time = get_number_from_line(race_times_str)
    race_distance = get_number_from_line(race_distances_str)

    number_of_ways_to_win_race = get_number_of_ways_to_win_race(race_time, race_distance)

    return number_of_ways_to_win_race


if __name__ == "__main__":

    input_file = open('input.txt', 'r')

    ways_to_win_race = get_number_of_ways_to_win_main_race(input_file)

    print("The number of ways to win the race is:", ways_to_win_race)