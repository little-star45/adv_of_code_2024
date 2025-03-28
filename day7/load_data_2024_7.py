def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(data_file):
    raw_data = load_data_from_file(data_file)
    results = []
    for row in raw_data.split('\n'):
        results.append(row)
    return results

def raw_data_tuple(data_file):
    raw_data = decode_data(data_file)
    results = []
    for x in raw_data:
        answer = int(x.split(":")[0])
        data = x.split(":")[1][1::].split(' ')
        data = [int(x) for x in data]
        results.append((answer, data))
    return results