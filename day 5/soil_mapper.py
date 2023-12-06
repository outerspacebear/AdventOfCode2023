
class MappedRange:
    destination_range_start = 0
    source_range_start = 0
    range_length = 0

    def __init__(self, dest_range_start, source_range_start, range_length):
        self.destination_range_start = dest_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length


def get_destination_value_from_map(source_value, map):

    for mapped_range in map:
        source_range_end = mapped_range.source_range_start + mapped_range.range_length - 1
        if source_value >= mapped_range.source_range_start and source_value <= source_range_end:
            return source_value + mapped_range.destination_range_start - mapped_range.source_range_start
        
    return source_value


def get_last_mapped_value_for_seed(seed, maps):

    source_value = seed

    for map in maps:
        source_value = get_destination_value_from_map(source_value, map)

    return source_value


def add_range_line_to_map(line, map):

    line_data = line.split()
    map.append(MappedRange(int(line_data[0]), int(line_data[1]), int(line_data[2])))
    return map


def get_maps(input_lines):

    maps = []
    current_map = []

    map_index = -1
    for line_index in range(2, len(input_lines)):
        
        if input_lines[line_index].isspace():
            maps.append(current_map)
            continue

        if 'map' in input_lines[line_index]:
            map_index += 1
            current_map = []
        else:
            current_map = add_range_line_to_map(input_lines[line_index], current_map)
    
    if len(current_map) > 0:
        maps.append(current_map)

    return maps


def get_seeds_from_input_string(line):

    seeds_str = line.split(':')[1]
    seeds_strs = seeds_str.split()
    seeds = [int(seed_str) for seed_str in seeds_strs]  
    return seeds

def find_lowest_location_for_initial_seeds(file):
    
    input_lines = input_file.readlines()

    input_seeds = get_seeds_from_input_string(input_lines[0])

    maps = get_maps(input_lines)

    last_destination_values = []
    for seed in input_seeds:
        last_destination_values.append(get_last_mapped_value_for_seed(seed, maps))

    return min(last_destination_values)
            


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    location = find_lowest_location_for_initial_seeds(input_file)
    print("The lowest location is:", location)