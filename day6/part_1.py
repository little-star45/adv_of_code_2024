"""If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
the guard will visit 41 distinct positions on your map."""
from load_data_2024_6 import decode_data

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
            
def get_guard_track(room, guard_start_pos):
    room = [list(res) for res in room]
    x, y = guard_start_pos
    steps = []
    turn = 'up'
    #'up', 'down', 'left', 'right'
    # '.' in ascii -> ord('.') = 46 ; ^ -> 94

    #add initial guard position
    steps.append(f'{x}_{y}')
    
    while (x != 0) and (y != 0) and (x != len(room[0])-1) and (y != len(room)-1):
        
        if turn == 'up':
            if ord(room[y-1][x]) in {46, 94}:
                y -=1
                steps.append(f'{x}_{y}')
            else:
                turn = 'right'        
                
        elif turn == 'down':
            if ord(room[y+1][x]) in {46, 94}:
                y +=1
                steps.append(f'{x}_{y}')
            else:
                turn = 'left'        
                
        elif turn == 'left':
            if ord(room[y][x-1]) in {46, 94}:
                x -=1
                steps.append(f'{x}_{y}')
            else:
                turn = 'up'

        elif turn == 'right':
            if ord(room[y][x+1]) in {46, 94}:
                x +=1
                steps.append(f'{x}_{y}')
            else:
                turn = 'down'
        
    return steps
            
def main(data_file):
    split_data = decode_data(data_file)
    guard_pos = get_guard_pos(split_data)
    guard_steps= get_guard_track(split_data, guard_pos)
    guard_diff_locations= len(set(guard_steps))

    return guard_diff_locations
    
if __name__ == '__main__':
    print(main('raw_data.txt'))
    # print(main('data_test.txt'))

#5242 ok