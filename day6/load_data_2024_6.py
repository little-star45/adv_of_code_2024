def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(data_file):
    raw_data = load_data_from_file(data_file)
    results = []
    for row in raw_data.split('\n'):
        results.append(row)
    return results