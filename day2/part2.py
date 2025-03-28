from load_data_2024_2 import prepare_data

def my_diff_function(data_trace):
    return [data_trace[i]-data_trace[i+1] for i in range(len(data_trace)-1)]

def if_increase_decrease(data_trace):
    diff = my_diff_function(data_trace)
    if (bugs:=len([x for x in diff if x<=0]))<=1: #for decrease
        if (bugs:=bugs+len([i for i in range(1,len(data_trace)-1) if data_trace[i-1]<data_trace[i+1]]))<=1:
            if (bugs:=bugs+len([x for x in diff if x>3]))<=1:
                return True
    bugs=0
    if (bugs:=len([x for x in diff if x>=0]))<=1: # for increase
        if (bugs:=bugs+len([i for i in range(1,len(data_trace)-1) if data_trace[i-1]>data_trace[i+1]]))<=1:
            if (bugs:=bugs+len([x for x in diff if x<(-3)]))<=1:
                return True
    return False

def main(data_file):
    data_matrix = prepare_data(data_file) #prepare data
    
    safe = 0

    for data_trace in data_matrix:

        res = if_increase_decrease(data_trace) #check if our data traces are fully increasing or deceasing
        if res==True:
            safe+=1

    return safe
            
if __name__ == '__main__':
    # test_function('problem_test.txt')
    # print(main('special_cases.txt'))
    print(main('problem_test.txt'))
    # print(main('data2.txt'))