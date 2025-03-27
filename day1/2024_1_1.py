from load_data_2024_1 import prepare_data

import random

def custom_quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        #median of three
        pivot = random.choice(arr)

        left=[x for x in arr if x<pivot]
        right=[x for x in arr if x>pivot]
        middle=[x for x in arr if x == pivot]

        return custom_quicksort(left) + middle + custom_quicksort(right)

def diff_locations_list(loc1,loc2):
    res_sum = 0
    if len(loc1)>len(loc2):
        for i in range(len(loc1)):
            res_sum += abs(loc1[i]-loc2[i])
    else:
        for i in range(len(loc2)):
            res_sum += abs(loc1[i]-loc2[i])
    return res_sum

def main(data_file):
    tab_left, tab_right = prepare_data(data_file)
    return diff_locations_list(custom_quicksort(tab_left),custom_quicksort(tab_right))

if __name__ == '__main__':
    try:
        print(main('day1/data1.txt'))
    except:
        print(main('data1.txt'))
    # #Right answer: 2066446

    # print(custom_quicksort([3,7]))