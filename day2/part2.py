from load_data_2024_2 import prepare_data

def my_diff_function(data_trace):
    return [data_trace[i]-data_trace[i+1] for i in range(len(data_trace)-1)]

def check_sorting(arr):
    return all(arr[i]<=arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(len(arr)-1))

def if_increase_decrease(data_trace):

    for i in range(len(data_trace)):
        temp_list= data_trace[:i]+data_trace[i+1:]

        if check_sorting(temp_list):
            diff_list = my_diff_function(temp_list)
            if all(-3 <= x <= 3 and x != 0 for x in diff_list):
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
    # print(main('problem_test.txt'))
    print(main('data2.txt'))