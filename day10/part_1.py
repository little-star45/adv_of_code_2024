"""
hiking trail is any path that starts at height 0, ends at height 9, 
and always increases by a height of exactly 1 at each step. Hiking 
trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).

I turn the queue. I will start from 9 to 0 and count it and next from 0 to 9 ant set its places into the tuple.

What is the sum of the scores of all trailheads on your topographic map?
"""

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(raw_data):
    results  = []
    for row in raw_data.split('\n'):
        results.append(list([int(x) for x in row]))
    return results

def from_zero_to_hero(dataset, start_nb):

    nb_in_row = []
    
    dat_rows = len(dataset) -1
    dat_cols = len(dataset[0]) -1

    sum_tracks = 0

    for i, row in enumerate(dataset):
        nb_in_row += [ (i,idx) for idx,nb in enumerate(row) if nb==start_nb]

    for nb in nb_in_row:
        print('start', nb)
        stp_x, stp_y = nb
        counter = 0

        for z in range(10):
            #left
            if stp_x-1 >= 0:
                if ((counter+1) == dataset[stp_y][stp_x-1]):
                    counter +=1
                    stp_x -=1
                    print('left',stp_x, stp_y, counter)
                    continue
            #right
            if stp_x+1 <= dat_cols:
                if ((counter+1) == dataset[stp_y][stp_x+1]):
                    counter +=1
                    stp_x +=1
                    print('right',stp_x, stp_y, counter)
                    continue
            #up
            if stp_y-1 >=0:
                if ((counter+1) == dataset[stp_y-1][stp_x]):
                    counter +=1
                    stp_y -=1
                    print('up',stp_x, stp_y, counter)
                    continue
            #down
            if stp_y+1 <= dat_rows:
                if ((counter+1) == dataset[stp_y+1][stp_x]):
                    counter +=1
                    stp_y +=1
                    print('down',stp_x, stp_y, counter)
                    continue

        if counter == 9:
            sum_tracks +=1
            counter = 0
    print('sum tracks', sum_tracks)

def main(data_file):
    raw_data = load_data_from_file(data_file)
    split_data = decode_data(raw_data)
    zeros = from_zero_to_hero(split_data, 0)
    
if __name__ == '__main__':
    # print(main('raw_data.txt'))
    print(main('data_test.txt'))
    # print(main('edge_cases.txt'))

#