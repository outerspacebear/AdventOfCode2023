
class MappedRange:
    destination_range_start = 0
    source_range_start = 0
    range_length = 0

    def __init__(self, dest_range_start, source_range_start, range_length):
        self.destination_range_start = dest_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

class SeedRange:
    range_start = 0
    range_length = 0

    def __init__(self, start, length):
        self.range_length = length
        self.range_start = start


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

    seeds = []

    print(len(seeds_strs))
    seed_text_index = -1
    while seed_text_index < len(seeds_strs):

        seed_text_index += 1
        if seed_text_index >= len(seeds_strs):
            break
        seed_range_start = int(seeds_strs[seed_text_index])
        seed_text_index += 1
        seed_range_length = int(seeds_strs[seed_text_index])

        print(seed_text_index, seed_range_start, seed_range_length)

        seeds.append(SeedRange(seed_range_start, seed_range_length))

    return seeds

def find_lowest_location_for_initial_seeds(file):
    
    input_lines = input_file.readlines()

    input_seeds = get_seeds_from_input_string(input_lines[0])

    maps = get_maps(input_lines)

    lowest_location = 0
    for seed_range in input_seeds:
        for seed in range(seed_range.range_start, seed_range.range_start + seed_range.range_length):
            last_mapped_value = get_last_mapped_value_for_seed(seed, maps)
            print(last_mapped_value)
            if lowest_location == 0 or last_mapped_value < lowest_location:
                lowest_location = last_mapped_value

    return lowest_location
            


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    location = find_lowest_location_for_initial_seeds(input_file)
    print("The lowest location is:", location)