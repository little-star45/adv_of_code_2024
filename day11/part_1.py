"""
blinking: 25 times
"""

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
        elif (len(str(nb))%2==0):
            half_nb = int((len(str(nb))/2))
            result.append(int(str(nb)[0:half_nb]))
            result.append(int(str(nb)[half_nb:]))
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
        temp_data = split_stone(sum_data)
        sum_data = temp_data
    # print(sum_data)

    return len(sum_data)

if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))
#211306 ; Thats the right answer :)