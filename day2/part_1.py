from load_data_2024_2 import prepare_data

def my_diff_function(data_trace):
    return [data_trace[i]-data_trace[i+1] for i in range(len(data_trace)-1)]

# def custom quicksort

def if_increase_decrease(data_trace):
    if data_trace[0]<data_trace[1]:
        return all(data_trace[i]<data_trace[i+1] for i in range(len(data_trace)-1))

    elif data_trace[0]>data_trace[1]:
        return all(data_trace[i]>data_trace[i+1] for i in range(len(data_trace)-1))
    return False

def main(data_file):
    safe = 0

    #prepare data
    data_matrix = prepare_data(data_file)
    
    #check all data matrix traces
    for data_trace in data_matrix:

        #calculate the diff between two element in each trace
        trace = my_diff_function(data_trace)
        print('trace',trace)
        #check if we don't have two same elements
        if 0 in trace:
            continue
        
        #sorted and chceck if we don't have too big spaces between numbers
        sorted_trace  = sorted(trace)
        print('sorted trace', sorted_trace)
        if (abs(sorted_trace[0])<=3 and abs(sorted_trace[-1]<=3)):
            print(data_trace)
            #check if our data traces are fully increasing or deceasing
            if (if_increase_decrease(data_trace)):
                safe +=1
    return safe
            
if __name__ == '__main__':
    # test_function('data1.txt')
    print(main('problem_test.txt'))
    # print(main('data1.txt'))

#Right answer: 407