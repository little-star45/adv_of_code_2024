def load_data_from_file(data_file):
    return open(data_file,'r').read()

def split_data(raw_data):
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

def prepare_data (data_file):
    raw_data = load_data_from_file(data_file)
    return split_data(raw_data)