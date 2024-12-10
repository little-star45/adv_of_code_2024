"""
0. Policzyc width i height mojej listy.
1. Bierzemy każdy element inny niż kropka i zczytuje jego polozenie.
2. Szukam czy cos lezy na ukosie lub w tej liniii gora dol.
3. Sprawdzam czy to to samo.
4. Zapisuje w liscie polozenie anteny dla obu przypadkow.
"""

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results = []
    for row in raw_data.split('\n'):
        results.append(list(row))
    return results

def search_anntennas(antennas_list, max_height, max_width):
    """Jezeli mam cos na pozycji (2,1) to diagonalnie node moze byc
    na pozycji (4,3) ale zawsze bedzie tak oddalona od obydwu punktow:
    czyli 3-5 = -2 i 4-5= -1, odejmuje x1-x2 oraz y1-y2; czyli x mniejsze o 1"""
    
    temp_antennas_list = []
    nodes_list = []
    # print(antennas_list)
    for antenna in antennas_list:
        # #check left-right
        # temp_antennas_list = [an for an in antennas_list if antenna[0][0]==an[0][0] and antenna != an and antenna[1]==an[1]]
        # # print(temp_antennas_list)

        # #check upside-down
        # temp_antennas_list = [an for an in antennas_list if antenna[0][1]==an[0][1] and antenna != an and antenna[1]==an[1]]
        # # print(temp_antennas_list)

        #check diagonal
        temp_antennas_list = [(antenna[0],an[0]) for an in antennas_list if antenna!=an and antenna[1]==an[1]]
        ##liczymy roznice na x i y
        ##sprawdzamy czy linia jest na x czy jest w lewo czy prawo i y czy dol czy gora
        ##dodajemy lub odejmujemy

        for pos in temp_antennas_list:
            #np. temp_antennas_list -> [((5, 5), (3, 4)), ((5, 5), (7, 6))]
            #np. pos -> ((5, 5), (3, 4))
            #pos_diff -> (y,x)

            pos_diff = (abs(pos[0][0]-pos[1][0]),abs(pos[0][1]-pos[1][1]))

            #liczymy funkcje liniowa i sprawdzamy czy jest malejaca czy rosnaca
            #ax1+b=y1, ax2+b=y2 -> b = y1-ax1, b = y2-ax2-> b=b -> ... -> a = y1-y2/(x1-x2); a>0 - mal, a<0 - ros -> tu bedzie na odwrot
            #bo jedziemy 0,0 gorny lewy rog a nie dolny lewy jak w kartezjanskim
            a = (pos[0][0]-pos[1][0]-1)/(pos[0][1]-pos[1][1])

            if a>0:
                #malejaca
                if pos[0][0]<pos[1][0]:
                    nodes_list.append((pos[0][0]-pos_diff[0],pos[0][1]-pos_diff[1]))
                    nodes_list.append((pos[1][0]+pos_diff[0],pos[1][1]+pos_diff[1]))
                else:
                    nodes_list.append((pos[1][0]-pos_diff[0],pos[1][1]-pos_diff[1]))
                    nodes_list.append((pos[0][0]+pos_diff[0],pos[0][1]+pos_diff[1]))
            elif a<0:
                #rosnaca
                if pos[0][0]<pos[1][0]:
                    
                    nodes_list.append((pos[0][0]-pos_diff[0],pos[0][1]+pos_diff[1]))
                    nodes_list.append((pos[1][0]+pos_diff[0],pos[1][1]-pos_diff[1]))
                else:
                    nodes_list.append((pos[1][0]-pos_diff[0],pos[1][1]+pos_diff[1]))
                    nodes_list.append((pos[0][0]+pos_diff[0],pos[0][1]-pos_diff[1]))

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
    # print('TEST NODE LIST: ', test_node_list)
    # print(nodes_list)
    return len(nodes_list)
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#249; That's the right answer!
