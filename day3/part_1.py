#It seems like the goal of the program is just to multiply some numbers.
#mul(x,y) -> x*y

import re

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    
    matches = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", raw_data)
    return matches

def del_mul(mul):
    return mul[4:-1].split(',')

def main(data_file):

    raw_data = load_data_from_file(data_file)
    matches = decode_data(raw_data)
    mul_nb_list = [del_mul(mul) for mul in matches]
    mul_multip = [int(x)*int(y) for x,y in mul_nb_list]

    return sum(mul_multip)


            
if __name__ == '__main__':
    # test_function('data1.txt')
    # print(main('data_test.txt'))
    print(main('data1.txt'))

# 185797128 That's the right answer :)
