"""
blinking: 25 times
"""

import numpy as np

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results  = raw_data.split(' ')
    return [int(x) for x in results]


def main(data_file):
    raw_data = load_data_from_file(data_file)
    start_data = decode_data(raw_data)

    blink_times = 75

    stones_list = np.array([], dtype=int)
    for i in np.nditer(np.array(range(blink_times))):
        print(i)
        stones_list = np.array([], dtype=int)
        for nb in np.nditer(np.array(start_data, dtype=int)):
            if (len(str(nb))%2==0):
                half_nb = len(str(nb))//2
                stones_list = np.ravel(np.append(stones_list,np.array([int(str(nb)[0:half_nb]), int(str(nb)[half_nb:])], dtype=int)))
            else:
                if (nb==0):
                    stones_list = np.ravel(np.append(stones_list,np.array([1], dtype=int)))
                else:
                    stones_list = np.ravel(np.append(stones_list,np.array([nb*2024], dtype=int)))
        start_data = stones_list

    return len(stones_list)

if __name__ == '__main__':
    # print(main('raw_data.txt'))
    print(main('data_test.txt'))
    # print(main('edge_cases.txt'))
#