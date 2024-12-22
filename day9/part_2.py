def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):

    return [x for x in raw_data]

def split_data_spaces(data):
    number = 0
    results=[]

    for i in range(len(data)):
        if i%2!=1:
            results.append([str(number) for x in range(int(data[i]))])
            number +=1
        else:
            results += ('.'*int(data[i]))
    
    results = [x for x in results if x!='']
    return results

def put_data_to_spaces(data):

    last_nb_idx = 0
    dot_nb = data.count('.')-1 #-1 because of last '.'
    dot_count = 0

    all_dot_occur_idx = [i for i, dot in enumerate(data) if dot=='.']

    new_data = data.copy()

    for i in range(len(data)):

        if (dot_count+1) == dot_nb:
            return [x for x in new_data if x != '.']
        
        last_nb_idx = int(len(new_data)-1-i)
        len_last_idx = len(new_data[last_nb_idx])

        dots_list = list('.'*len_last_idx)

        for dot_idx in all_dot_occur_idx:

            # print(new_data[dot_idx:dot_idx+len_last_idx], new_data[last_nb_idx])
            if (new_data[last_nb_idx] != '.') and (new_data[dot_idx:dot_idx+len_last_idx] == dots_list) and (new_data[last_nb_idx] != '+'):
                new_data[dot_idx] = new_data[last_nb_idx] #put my numbers list into first dot place
                new_data[dot_idx+1:dot_idx+len_last_idx] = list('+'*(len(dots_list)-1)) #fill another dot places with +, only for stop put here things later
                new_data[last_nb_idx] = dots_list #replace last numer in empty dot
                dot_count +=1
                all_dot_occur_idx = [i for i, dot in enumerate(new_data[:last_nb_idx]) if dot=='.']
                break
            elif (new_data[last_nb_idx] == '.'):
                break
    clear_new_data = [element for element in new_data if (element != '+')]
    dots_to_lists = [element if (element != '.') else ['.'] for element in clear_new_data ]

    return sum(dots_to_lists, [])
    
def calculate_checksum(data):
    results = 0

    for i, element in enumerate(data):
        
        if element != '.':
            
            results += i*int(element)
    return results

def main(data_file):
    raw_data = load_data_from_file(data_file)
    split_data = decode_data(raw_data)
    disk_map = split_data_spaces(split_data)
    data_in_spaces = put_data_to_spaces(disk_map)
    print(max(data_in_spaces))
    print(data_in_spaces)
    checksum = calculate_checksum(data_in_spaces)
    return checksum
    
if __name__ == '__main__':
    #84540008440
    # print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    print(main('edge_cases.txt'))

#6381625079736; That's not the right answer; your answer is too high.
#6381624803796 - right