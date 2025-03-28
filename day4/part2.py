from load_data_2024_4 import decode_data

def xmas_diagonal_right(word, input, all_data, row_nb, search_letter):
    #search letter - first letter from left to right
    # [ 0, 1,
    #   2, 3 ]
    # [MM
    #  SS] without A becouse A is alwase in the middle
    x_idx = 0
    xmas_counter = 0
    
    for i in range(input.count(search_letter)):

        x_idx = input.index(search_letter, x_idx)
        if  x_idx <len(input)-2: #down right
            if [
                all_data[row_nb][x_idx],
                all_data[row_nb+1][x_idx+1],
                all_data[row_nb+2][x_idx+2]
                ] == [word[0],'A',word[3]]:
                if [
                    all_data[row_nb][x_idx+2],
                    all_data[row_nb+1][x_idx-1+2],
                    all_data[row_nb+2][x_idx-2+2]
                    ] == [word[1],'A',word[2]]:
                    xmas_counter +=1
        
        x_idx +=1
    return xmas_counter

def main(data_file):
    xmas_counter = 0
    data_list = decode_data(data_file)

    for i, data_slice in enumerate(data_list):
        
        if(i<len(data_list)-2):
            xmas_counter += xmas_diagonal_right(['M','S','M','S'], data_slice, data_list, i, 'M')
            xmas_counter += xmas_diagonal_right(['M','M','S','S'], data_slice, data_list, i, 'M')
            xmas_counter += xmas_diagonal_right(['S','S','M','M'], data_slice, data_list, i, 'S') 
            xmas_counter += xmas_diagonal_right(['S','M','S','M'], data_slice, data_list, i, 'S')  

    return xmas_counter
            
if __name__ == '__main__':
    print(main('data1.txt'))
    #1815 That's the right answer!;
    

