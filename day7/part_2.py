from load_data_2024_7 import raw_data_tuple
from itertools import product
from math import prod

def get_variants(data):
    return set(list(product(['*', '+', '||'], repeat = (len(data)-1))))

def check_datatrace(data):
    answer = data[0]
    numbers = data[1]

    #all multiply
    results = prod(numbers)

    if (results==answer):
        return answer
    
    #all add
    results = 0
    if (sum(numbers)==answer):
        return answer

    #if * or + or ||
    sign_possibility = get_variants(numbers)

    for sign_trace in sign_possibility:

        numbers = data[1]
        results = numbers[0]

        for i, sign in enumerate(sign_trace):
            
            if (sign=='+'):
                results += numbers[i+1]
                if results > answer:
                    break
            elif (sign=="||"):
                results = int(str(results)+str(numbers[i+1]))
            else:
                results *= numbers[i+1]
                if results > answer:
                    break
        if (results==answer):
            return answer
        
    return 0


def main(data_file):
    data_tuple = raw_data_tuple(data_file)

    res_sum = 0
    for i, data in enumerate(data_tuple):
        print(f'{i+1}/{len(data_tuple)}')
        res_sum += check_datatrace(data)

    return res_sum
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#34612812972206 That's the right answer!