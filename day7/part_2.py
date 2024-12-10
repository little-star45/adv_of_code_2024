from itertools import product

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results = []
    for row in raw_data.split('\n'):
        results.append(row)
    return results

def raw_data_tuple(split_data):
    results = []
    for x in split_data:
        answer = int(x.split(":")[0])
        data = x.split(":")[1][1::].split(' ')
        data = [int(x) for x in data]
        results.append((answer, data))
    return results

def get_variants(data):
    return set(list(product(['*', '+', '||'], repeat = (len(data)-1))))

def check_datatrace(data):
    answer = data[0]
    numbers = data[1].copy()

    #all multiply
    results = 1
    for val in numbers:
        results *= val

    if (results==answer):
        return answer
    
    #all add
    results = 0
    if (sum(numbers)==answer):
        return answer

    #if * or + or ||
    sign_possibility = get_variants(numbers)

    for sign_trace in sign_possibility:

        numbers = data[1].copy()
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
    raw_data = load_data_from_file(data_file)
    split_data = decode_data(raw_data)
    data_tuple = raw_data_tuple(split_data)

    res_sum = 0
    for i, data in enumerate(data_tuple):
        print(f'{i+1}/{len(data_tuple)}')
        res_sum += check_datatrace(data)

    return res_sum
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#34612812972206 That's the right answer! You are one gold star;