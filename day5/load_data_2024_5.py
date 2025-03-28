def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(data_file):
    raw_data = load_data_from_file(data_file)
    code, pages = [], []
    for row in raw_data.split('\n'):
        if '|' in row:
            code.append(row)
        else:
            pages.append(row)
    del pages[0]
    return code, pages