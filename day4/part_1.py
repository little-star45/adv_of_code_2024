def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results = []
    for row in raw_data.split('\n'):
        results.append(list(row))
    return results

def xmas_right(word, input, reverse = False):
    x_idx = 0
    xmas_counter = 0

    for i in range(input.count('X')):
        x_idx = input.index('X', x_idx)
        if reverse == False:
            if input[x_idx:x_idx+4] == word:
                xmas_counter +=1
        if reverse == True:
            if [input[x_idx],input[x_idx-1],input[x_idx-2],input[x_idx-3] ] == word:
                xmas_counter +=1
        x_idx +=1
    return xmas_counter

def xmas_down(word, input, all_data, row_nb, reverse = False):
    x_idx = 0
    xmas_counter = 0

    for i in range(input.count('X')):
        x_idx = input.index('X', x_idx)
        if reverse == False:
            if [all_data[row_nb][x_idx],all_data[row_nb+1][x_idx],all_data[row_nb+2][x_idx],all_data[row_nb+3][x_idx]] == word:
                xmas_counter +=1

        if reverse == True:
            if [all_data[row_nb][x_idx],all_data[row_nb-1][x_idx],all_data[row_nb-2][x_idx],all_data[row_nb-3][x_idx]] == word:
               xmas_counter +=1
        
        x_idx +=1
    return xmas_counter

def xmas_diagonal(word, input, all_data, row_nb, reverse = False):
    x_idx = 0
    xmas_counter = 0
    
    for i in range(input.count('X')):
        x_idx = input.index('X', x_idx)

        if reverse == False:
            if  x_idx <len(input)-3: #down right
                if [all_data[row_nb][x_idx],all_data[row_nb+1][x_idx+1],all_data[row_nb+2][x_idx+2],all_data[row_nb+3][x_idx+3]] == word:
                    xmas_counter +=1
            if x_idx>2: #down left
                if [all_data[row_nb][x_idx],all_data[row_nb+1][x_idx-1],all_data[row_nb+2][x_idx-2],all_data[row_nb+3][x_idx-3]] == word:
                    xmas_counter +=1

        if reverse == True:
            if  x_idx <len(input)-3: #up right
                if [all_data[row_nb][x_idx],all_data[row_nb-1][x_idx+1],all_data[row_nb-2][x_idx+2],all_data[row_nb-3][x_idx+3]] == word:
                    xmas_counter +=1
            
            if x_idx >2: #up left
                if [all_data[row_nb][x_idx],all_data[row_nb-1][x_idx-1],all_data[row_nb-2][x_idx-2],all_data[row_nb-3][x_idx-3]] == word:
                    xmas_counter +=1
        
        x_idx +=1
    return xmas_counter


def main(data_file):
    xmas_counter = 0
    raw_data = load_data_from_file(data_file)
    data_list = decode_data(raw_data)

    for i, data_slice in enumerate(data_list):
        xmas_counter += xmas_right(['X','M','A','S'], data_slice)
        xmas_counter += xmas_right(['X','M','A','S'], data_slice, reverse=True)

        if(i<len(data_list)-3):
            xmas_counter += xmas_down(['X','M','A','S'], data_slice, data_list, i)
            xmas_counter += xmas_diagonal(['X','M','A','S'], data_slice, data_list, i)
        if(i>2):
            xmas_counter += xmas_down(['X','M','A','S'], data_slice, data_list, i, reverse=True)
        if(i>2):
            xmas_counter += xmas_diagonal(['X','M','A','S'], data_slice, data_list, i, reverse=True)

    return xmas_counter
            
if __name__ == '__main__':
    print(main('data1.txt'))

    #2336 That's not the right answer; your answer is too low.
    #2345

