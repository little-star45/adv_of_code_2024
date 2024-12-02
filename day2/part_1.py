def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    
    raw_data_to_list = raw_data.split(' ')
    raw_data_into_matrix = []
    temp_data = []
    for data in raw_data_to_list:
        if '\n' in data:
            temp_data.append(int(data.split('\n')[0]))
            raw_data_into_matrix.append(temp_data)
            temp_data = []
            temp_data.append(int(data.split('\n')[-1]))
        else:
            temp_data.append(int(data))
    raw_data_into_matrix.append(temp_data)
    return raw_data_into_matrix

def my_diff_function(data_trace):
    test_list = []

    for i in range(len(data_trace)-1):
        test_list.append(int(data_trace[i])-int(data_trace[i+1]))
    return test_list

def if_increase_decrease(data_trace):
    print(data_trace)
    variant = ''
    if len(data_trace)>=2:
        if data_trace[0]<data_trace[1]:
            variant = 'increase'
        elif data_trace[0]>data_trace[1]:
            variant = 'decrease'
        else:
            return False

    for i in range(len(data_trace)-1):
        print(data_trace[i],data_trace[i+1])
        if (variant == 'increase'):
            if data_trace[i]<data_trace[i+1]:
                continue
            else:
                return False
        elif (variant == 'decrease'):
            if data_trace[i]>data_trace[i+1]:
                continue
            else:
                return False
    return True

def main(data_file):

    raw_data = load_data_from_file(data_file)
    data_matrix = decode_data(raw_data)

    safe = 0

    for data_trace in data_matrix:

        trace = my_diff_function(data_trace)
        if 0 in trace:
            continue

        sorted_trace  = sorted(trace)

        if (abs(sorted_trace[0])<=3 and abs(sorted_trace[-1]<=3)):
            print(data_trace)
            if (if_increase_decrease(data_trace)):
                safe +=1
    return safe
            
if __name__ == '__main__':
    # test_function('data1.txt')
    # print(main('data_test.txt'))
    print(main('data1.txt'))

# 327 That's not the right answer; your answer is too low

#Right answer: 407