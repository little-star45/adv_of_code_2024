def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results = []
    for row in raw_data.split('\n'):
        results.append(list(row))
    return results

def search_anntennas(antennas_list, max_height, max_width):
    
    temp_antennas_list = []
    nodes_list = []
    # print(antennas_list)
    for antenna in antennas_list:
        
        #check diagonal
        temp_antennas_list = [(antenna[0],an[0]) for an in antennas_list if antenna!=an and antenna[1]==an[1]]

        for pos in temp_antennas_list:
            #np. temp_antennas_list -> [((5, 5), (3, 4)), ((5, 5), (7, 6))]
            #np. pos -> ((5, 5), (3, 4))
            #pos_diff -> (y,x)

            pos_diff = (abs(pos[0][0]-pos[1][0]),abs(pos[0][1]-pos[1][1]))

            a = (pos[0][0]-pos[1][0]-1)/(pos[0][1]-pos[1][1])

            if a>0:
                i=1
                while i<int(max_height*pow(2,0.5))+1:
                    #malejaca
                    nodes_list.append((pos[0][0]-i*pos_diff[0],pos[0][1]-i*pos_diff[1]))
                    nodes_list.append((pos[1][0]+i*pos_diff[0],pos[1][1]+i*pos_diff[1]))
                    nodes_list.append((pos[1][0]-i*pos_diff[0],pos[1][1]-i*pos_diff[1]))
                    nodes_list.append((pos[0][0]+i*pos_diff[0],pos[0][1]+i*pos_diff[1]))
                    i +=1
            elif a<0:
                i=1
                while i<int(max_height*pow(2,0.5))+1:
                #rosnaca
                    nodes_list.append((pos[0][0]-i*pos_diff[0],pos[0][1]+i*pos_diff[1]))
                    nodes_list.append((pos[1][0]+i*pos_diff[0],pos[1][1]-i*pos_diff[1]))
                    nodes_list.append((pos[1][0]-i*pos_diff[0],pos[1][1]+i*pos_diff[1]))
                    nodes_list.append((pos[0][0]+i*pos_diff[0],pos[0][1]-i*pos_diff[1]))
                    i +=1

    set_bound = [node for node in list(set(nodes_list)) if (node[0]<max_height) and (node[1]<max_width) and (node[0]>=0) and (node[1]>=0)]
    return set_bound
    
def main(data_file):
    raw_data = load_data_from_file(data_file)
    split_data = decode_data(raw_data)
    
    #0
    max_width = len(split_data[0])
    max_height = len(split_data)

    #1
    antennas_list = []
    test_node_list = []

    for y in range(max_height):
        for x in range(max_width):
            if split_data[y][x] != '.' and split_data[y][x] != '#':
                antennas_list.append(((y,x),split_data[y][x]))

    for y in range(max_height):
        for x in range(max_width):
            if split_data[y][x] == '#':
                test_node_list.append(((y,x)))

    nodes_list = search_anntennas(antennas_list, max_height, max_width)

    return len(nodes_list)
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#807; That's not the right answer; your answer is too low.
#905; That's the right answer!