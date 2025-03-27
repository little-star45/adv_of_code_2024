from load_data_2024_1 import prepare_data
from collections import Counter

def calc_similarity(l_tab, similar_tab):
    counter_dict=Counter(similar_tab)
    res_similarity=0

    for nb in set(l_tab):
        res_similarity += nb*counter_dict[nb]
    return res_similarity

def main(data_file):
    tab_left, tab_right = prepare_data(data_file)
    return calc_similarity(tab_left,tab_right)
     
if __name__ == '__main__':
    try:
        print(main('day1/data1.txt'))
    except:
        print(main('data1.txt'))
    #Right answer: 24931009