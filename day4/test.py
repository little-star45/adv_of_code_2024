import pytest
import part_1
import part2

# def test_get_basic_xmas():
#     result = part_1.main('data_test.txt')
#     assert result == 18

#python -m pytest test.py -vvv

def test_get_basic_xmas_right():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for data_slice in data_list:
        xmas_counter += part_1.xmas_right(['X','M','A','S'], data_slice)
    assert xmas_counter == 3

def test_get_basic_xmas_right_reverse():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for data_slice in data_list:
        xmas_counter += part_1.xmas_right(['X','M','A','S'], data_slice, reverse=True)
    assert xmas_counter == 2

def test_get_basic_xmas_down():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for i, data_slice in enumerate(data_list):
        if(i<len(data_list)-3):
            xmas_counter += part_1.xmas_down(['X','M','A','S'], data_slice, data_list, i)
    assert xmas_counter == 1

def test_get_basic_xmas_down_reverse():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for i, data_slice in enumerate(data_list):
        if(i>3):
            xmas_counter += part_1.xmas_down(['X','M','A','S'], data_slice, data_list, i, reverse=True)
    assert xmas_counter == 2


def test_get_basic_xmas_diagonal():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for i, data_slice in enumerate(data_list):
        if(i<len(data_list)-3):
            xmas_counter += part_1.xmas_diagonal(['X','M','A','S'], data_slice, data_list, i)
    assert xmas_counter == 2

def test_get_basic_xmas_diagonal():
    #XMAS
    raw_data = part_1.load_data_from_file('data_test.txt')
    data_list = part_1.decode_data(raw_data)
    xmas_counter = 0
    for i, data_slice in enumerate(data_list):
        if(i>3):
            xmas_counter += part_1.xmas_diagonal(['X','M','A','S'], data_slice, data_list, i, reverse=True)
    assert xmas_counter == 8

def test_get_advance_x_mas_diagonal():
    raw_data = part2.load_data_from_file('data_test.txt')
    data_list = part2.decode_data(raw_data)
    xmas_counter = 0
    for i, data_slice in enumerate(data_list):
        
        if(i<len(data_list)-2):
            xmas_counter += part2.xmas_diagonal_right(['M','S','M','S'], data_slice, data_list, i, 'M')
            xmas_counter += part2.xmas_diagonal_right(['M','M','S','S'], data_slice, data_list, i, 'M')
            xmas_counter += part2.xmas_diagonal_right(['S','S','M','M'], data_slice, data_list, i, 'S')
            xmas_counter += part2.xmas_diagonal_right(['S','M','S','M'], data_slice, data_list, i, 'S')
    assert xmas_counter == 9