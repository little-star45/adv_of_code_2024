from pprint import pprint
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
        test_list.append(abs(int(data_trace[i])-int(data_trace[i+1])))
    return test_list

def if_increase_decrease(data_trace):

    for i in range(len(data_trace)-1):

        if (sorted(data_trace)==data_trace) or (sorted(data_trace, reverse=True)==data_trace):
            if (len(set(data_trace))>=len(data_trace)-1) and sorted(my_diff_function(data_trace), reverse=True)[0]<=3:
                return True
        
        for j, x in enumerate(data_trace):
            temp_list = data_trace.copy()
            temp_list.pop(j)
            if (sorted(temp_list)==temp_list) or (sorted(temp_list, reverse=True)==temp_list):
                if sorted(my_diff_function(temp_list), reverse=True)[0]<=3:
                    return True
                
        return False

def main2(data_file):
    raw_data = load_data_from_file(data_file)
    data_matrix = decode_data(raw_data)

    print(data_matrix)

    #usuniecie powielonych wiecej niz jeden raz
    bez_powielonych = [x for x in data_matrix if len(set(x))>=(len(x)-1)]

    #usuniecie gdy wiecej niz jeden diff powyzej 3
    trace = [x for x in bez_powielonych if sorted(my_diff_function(x), reverse=True)[1]<=3]
    
    safe = 0

    test_trace = []
    for data_trace in trace:
        if (if_increase_decrease(data_trace)):
            safe +=1
            test_trace.append(True)
        else:
            test_trace.append(False)

    return safe
            
if __name__ == '__main__':
    # test_function('problem_test.txt')
    # print(main('data_test.txt'))
    pprint(main2('data2.txt'))

# 426 That's not the right answer; your answer is too low.
# 486 That's not the right answer; your answer is too high.

# 481
# 436 That's not the right answer; your answer is too low.
# 477 That's not the right answer;
# 444 That's not the right answer;
# 464 That's not the right answer;
# 462 That's not the right answer;

#Right answer: 407