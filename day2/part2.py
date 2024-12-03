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
        test_list.append(int(data_trace[i])-int(data_trace[i+1]))
    return test_list

def if_increase_decrease(data_trace):
    nb_equal = 0
    nb_increase = 0
    nb_decrease = 0
    errors = 0

    for i in range(len(data_trace)-1):

        # if (abs(data_trace[i]-data_trace[i+1])>3):
        #     errors +=1       
        if data_trace[i]<data_trace[i+1]:
            nb_increase +=1
        elif data_trace[i]>data_trace[i+1]:
            nb_decrease +=1
        else:
            nb_equal +=1
 
    if (errors>1):
        return False
    elif (nb_equal>2):
        return False
    elif (nb_equal==1 and errors!=0):
        return False
    elif((nb_increase==len(data_trace)-1)):
        return True
    elif ((nb_decrease==len(data_trace)-1)):
        return True
    elif ((nb_increase==len(data_trace)-2)and (nb_decrease==1 or nb_equal==1)):

        for i in range(len(data_trace)-1):
            if data_trace[i]>data_trace[i+1]:
                data_trace.pop(i)
                break

        for i in range(len(data_trace)-1):
            if data_trace[i]<data_trace[i+1]:
                continue
            else:
                return False
        return True
    
    elif ((nb_decrease==len(data_trace)-2)and (nb_increase==1 or nb_equal==1)): 

        for i in range(len(data_trace)-1):
            if data_trace[i]<data_trace[i+1]:
                data_trace.pop(i)
                break

        for i in range(len(data_trace)-1):
            if data_trace[i]>data_trace[i+1]:
                continue
            else:
                return False
        return True
    else:         
        return False

def main(data_file):

    raw_data = load_data_from_file(data_file)
    data_matrix = decode_data(raw_data)

    safe = 0

    for data_trace in data_matrix:

        trace = my_diff_function(data_trace)

        if (if_increase_decrease(data_trace)):
            safe +=1

        print('data_trace:',data_trace, 'safe:', safe)

    return safe

def main2(data_file):
    raw_data = load_data_from_file(data_file)
    data_matrix = decode_data(raw_data)

    #usuniecie powielonych wiecej niz jeden raz
    bez_powielonych = [x for x in data_matrix if len(set(x))>=(len(x)-1)]

    #usuniecie gdy wiecej niz jeden diff powyzej 3
    trace = [x for x in bez_powielonych if sorted(my_diff_function(x), reverse=True)[1]<=3]
    
    clear_dec_asc = []

    #znalezienie czystych wzrastajacych lub opadajacych
    for element in trace:
        if (sorted(element) == element) or (sorted(element, reverse=True) == element):
            clear_dec_asc.append(element)
    return clear_dec_asc, len(clear_dec_asc)
            
if __name__ == '__main__':
    # test_function('problem_test.txt')
    # print(main('data_test.txt'))
    pprint(main2('data2.txt'))

# 426 That's not the right answer; your answer is too low.
# 486 That's not the right answer; your answer is too high.
# 436 That's not the right answer; your answer is too low.
# 477 That's not the right answer;
# 444 That's not the right answer;

#Right answer: 407