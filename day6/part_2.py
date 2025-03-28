"""If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
the guard will visit 41 distinct positions on your map."""

"""
1. Put the stars in every step. (without initial position)
2. Calc everything.
2.1 Check if make three right turns in a row.
"""
from load_data_2024_6 import decode_data
from part_1 import get_guard_track

def get_guard_pos(split_data):
    x = 0
    for y,data in enumerate(split_data):
        if '^' in data:
            x = data.index('^')
            return (x,y)
            
def buckup_in_file(room_buckup):
    with open('buckup_list.txt', 'w') as f:
        for line in room_buckup:
            f.write("%s\n" % ('').join(line))

def check_guard_stuck(room, guard_start_pos, o_x, o_y, guard_steps):

    room = [list(res) for res in room]
    room[o_y][o_x] = '#'

    x, y = guard_start_pos
    turns = []
    turn = 'up'
    
    while (x != 0) and (y != 0) and (x != len(room[0])-1) and (y != len(room)-1):

        #You can use fields that you can't use before!
        
        if turn == 'up':
            if ((ord(room[y-1][x]) == 46) or (ord(room[y-1][x]) == 94)):
                y -=1
            else:
                turn = 'right'
                
                if turns.count(f'{x}_{y}')>2:
                    return True
                turns.append(f'{x}_{y}')

        elif turn == 'down':
            if ((ord(room[y+1][x]) == 46) or (ord(room[y+1][x]) == 94)):
                y +=1
            else:
                turn = 'left'  
                if turns.count(f'{x}_{y}')>2:
                    return True
                turns.append(f'{x}_{y}')
                
        elif turn == 'left':
            if ((ord(room[y][x-1]) == 46) or (ord(room[y][x-1]) == 94)):
                x -=1
            else:
                turn = 'up'
                if turns.count(f'{x}_{y}')>2:
                    return True
                turns.append(f'{x}_{y}')    

        elif turn == 'right':
            if ((ord(room[y][x+1]) == 46) or (ord(room[y][x+1]) == 94)):
                x +=1
            else:
                turn = 'down'
                if turns.count(f'{x}_{y}')>2:
                    return True
                turns.append(f'{x}_{y}')
        # you can go through any of field max 2 times
    return False
            
def main(data_file):
    split_data = decode_data(data_file)
    guard_pos = get_guard_pos(split_data)
    guard_steps = get_guard_track(split_data, guard_pos)

    guard_diff_locations= list(set(guard_steps))
 
    len_guars_stps = len(guard_diff_locations)
    o_locations_nb = 0

    for i, pos in enumerate(guard_diff_locations):
        print(f'{i+1}/{len_guars_stps}')
        x_o, y_o = int(pos.split('_')[0]), int(pos.split('_')[1])
        location_catch = check_guard_stuck(split_data, guard_pos,x_o, y_o, guard_diff_locations)

        if location_catch:
            o_locations_nb += 1

    return o_locations_nb
    
if __name__ == '__main__':
    # print(main('data_test.txt'))
    print(main('raw_data.txt'))

#1424 That's the right answer;
