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

def prepare_data (data_file):
    raw_data = load_data_from_file(data_file)
    return decode_data(raw_data)