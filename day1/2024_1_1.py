def load_data_from_file(data_file):
    return open(data_file,'r').read()

def split_data_into_lists(raw_data):
    tab1, tab2 = [],[]
    line_data = raw_data.split('\n')
    for trace in line_data:
        split_trace = trace.split('   ')
        if len(split_trace)>0:
            tab1.append(int(split_trace[0]))
            tab2.append(int(split_trace[1]))
        else:
            tab1.append(int(split_trace[0]))
    return tab1, tab2

def diff_locations_list(loc1,loc2):
    results_list =[]
    if len(loc1)>len(loc2):
        for i in range(len(loc1)):
            results_list.append(abs(loc1[i]-loc2[i]))
    else:
        for i in range(len(loc2)):
            results_list.append(abs(loc1[i]-loc2[i]))
    return results_list

def main(data_file):
    raw_data = load_data_from_file(data_file)
    tab1, tab2 = split_data_into_lists(raw_data)
    diff_loc = diff_locations_list(sorted(tab1),sorted(tab2))
    return sum(diff_loc)

if __name__ == '__main__':
    # print(main('data_test.txt'))
    print(main('data1.txt'))
    #Right answer: 2066446