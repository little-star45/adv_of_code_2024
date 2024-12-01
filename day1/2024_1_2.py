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

def calc_similarity(l_tab, similar_tab):
    res_similarity=[]
    for nb in l_tab:
        res_similarity.append(nb*similar_tab.count(nb))
    return res_similarity

def main(data_file):
    raw_data = load_data_from_file(data_file)
    tab1, tab2 = split_data_into_lists(raw_data)
    sim_tab = calc_similarity(tab1,tab2)
    return sum(sim_tab)

if __name__ == '__main__':
    # print(main('data_test.txt'))
    print(main('data1.txt'))
    #Right answer: 24931009