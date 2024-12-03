#It seems like the goal of the program is just to multiply some numbers.
#mul(x,y) -> x*y

import re

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):

    mul_idx = [m.start() for m in re.finditer(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", raw_data)]
    do_idx = [m.start() for m in re.finditer(r"do\(\)", raw_data)]
    do_idx.insert(0,0)
    dont_idx = [m.start() for m in re.finditer(r"don\'t\(\)", raw_data)]

    return mul_idx, do_idx, dont_idx

def del_mul(mul):
    return mul[4:-1].split(',')

def get_mul_indexes(mul_idx, do_idx, dont_idx):
    l_bound = do_idx[0]
    brackets = []
    id = 0
    ib = 0

    #good ranges
    if do_idx[-1] > dont_idx[-1]:
        do_idx.append(mul_idx[-1]+1)

    while (dont_idx[ib]!=dont_idx[-1]) or (do_idx[id]!=do_idx[-1]):
        if dont_idx[ib]>do_idx[id]:
            id +=1
        else:
            if l_bound<dont_idx[ib]:
                brackets.append((l_bound,dont_idx[ib]))
                l_bound = do_idx[id]
                id +=1
            ib +=1

    if do_idx[id] < dont_idx[ib]:
        brackets.append((l_bound,dont_idx[ib]))
    else:
        brackets.append((l_bound,do_idx[id]))

    range_idx = 0
    good_mull = []
    #good ranges implemented into mul_idx

    for i, mul in enumerate(mul_idx):
        if (mul >=brackets[range_idx][0]) and (mul< brackets[range_idx][1]):
            good_mull.append(i)
        else:
            if mul>brackets[range_idx][1]:
                range_idx +=1
    # print(mul_idx)

    print('good_mull len:', len(good_mull))
    return good_mull

def main(data_file):

    raw_data = load_data_from_file(data_file)
    mul_idx, do_idx, dont_idx = decode_data(raw_data)
    good_mull_idx = get_mul_indexes(mul_idx, do_idx, dont_idx)

    matches = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", raw_data)

    #get index and immedietly turn it into tuple mul(x,y) => (x,y)
    mul_nb_list = [del_mul(matches[mul_nb]) for mul_nb in good_mull_idx]

    mul_multip = [int(x)*int(y) for x,y in mul_nb_list]

    return sum(mul_multip)


            
if __name__ == '__main__':
    # test_function('data1.txt')
    # print(main('data_test.txt'))
    print(main('data2.txt'))

# 185797128 That's the right answer :)
# 89798695 That's the right answer! :)
