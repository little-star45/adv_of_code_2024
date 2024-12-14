def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):

    return [x for x in raw_data]

def split_data_spaces(data):
    number = 0
    results=[]

    for i in range(len(data)):
        if i%2!=1:
            results += [str(number) for x in range(int(data[i]))]
            number +=1
        else:
            results += list('.'*int(data[i]))
    return results

def put_data_to_spaces(data):
    
    first_dot_idx = 0
    last_nb_idx = 0
    dot_nb = data.count('.')-1 #-1 because of last '.'
    dot_count = 0

    for i in range(len(data)):
        if (dot_count+1) == dot_nb:
            return [x for x in data if x != '.']
        
        first_dot_idx = data.index('.')
        last_nb_idx = int(len(data)-1-i)

        if data[last_nb_idx] != '.':  
            data[first_dot_idx] = data[last_nb_idx]
            data[last_nb_idx] = '.'
            dot_count +=1
    
def calculate_checksum(data):
    results = 0

    for i, element in enumerate(data):
        results += i*int(element)
    return results

def main(data_file):
    raw_data = load_data_from_file(data_file)
    split_data = decode_data(raw_data)
    disk_map = split_data_spaces(split_data)
    data_in_spaces = put_data_to_spaces(disk_map)
    checksum = calculate_checksum(data_in_spaces)

    return checksum
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#90167081070 ;  your answer is too low
#6359213660505 ; That's the right answer!