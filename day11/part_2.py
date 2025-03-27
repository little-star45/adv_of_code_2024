"""
blinking: 25 times
"""
from math import log10, floor, modf, ceil

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results  = raw_data.split(' ')
    return [int(x) for x in results]

def split_stone(raw_data):

    result = []

    for nb in raw_data:
        if (nb==0):
            result.append(1)
        elif (nb_digits := (floor(log10(nb)) + 1)) % 2 == 0:
            nb_parts = str(nb/(10**(nb_digits//2))).split('.')
            result.append(int(nb_parts[0]))
            result.append(int(nb_parts[1]))
        else:
            result.append(nb*2024)
    return result

def main(data_file):
    raw_data = load_data_from_file(data_file)
    start_data = decode_data(raw_data)
    print(start_data)

    sum_data = start_data
    temp_data = []

    blink_times = 25

    for i in range(blink_times):
        print(f"{i+1}/25")
        temp_data = split_stone(sum_data)
        # print(temp_data)
        sum_data = temp_data
    print(sum_data)

    return len(sum_data)

if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))
#211306 ; Thats the right answer :)