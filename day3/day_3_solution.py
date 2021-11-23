
import os
from numpy import prod

def print_x(x, my_list):
    """Print up to x elements of list"""
    num = min(x, len(my_list))
    for i in range(num):
        print(my_list[i])


def print_n_chars_x(n: int, x: int, my_list: list):
    """Print first n characters of up to x elements of list"""
    num = min(x, len(my_list))
    for i in range(num):
        chars = min(n, len(my_list[i]))
        print(my_list[i][:chars])


def show_last_x_lines(x: int, lines: list):
    """Print first n characters of up to x elements of list"""
    last_x_lines = lines[-x:]
    mid_point = round(x/2)
    if "X" in last_x_lines[mid_point]:
        mid_char = last_x_lines[mid_point].index("X")
    else:
        mid_char = last_x_lines[mid_point].index("O")
    print(mid_char)
    for i in last_x_lines:
        print(i[(mid_char-40):(mid_char+40)])
        

# x = 1 for line 1
def check_slope(right: int, down: int):

    with open("input.txt", encoding='utf-8') as file:
        lines = file.read().splitlines()

    lines = [x * 100 for x in lines]

    x = 1
    traversed = []
    hit_tree = []
    for count, line in enumerate(lines):
        if count % down == 0:
            x = int(count / down * right)
            if line[x] == "#":
                hit_tree.append(True)
                traversed_line = line[:x] + "X" + line[x:]
                traversed.append(traversed_line)
            elif line[x] == ".":
                hit_tree.append(False)
                traversed_line = line[:x] + "O" + line[x:]
                traversed.append(traversed_line)
            else:
                assert(False == True)
        else:
            traversed.append(line)

    num_hit = hit_tree.count(True)
    num_avoided = hit_tree.count(False)
    print(f'Right: {right}, down: {down}, num_hit: {num_hit}, num_avoided: {num_avoided}, total: {num_hit+num_avoided}')
    return(num_hit)

check_all = [check_slope(1,1),check_slope(3,1),check_slope(5,1),check_slope(7,1),check_slope(1,2)]
print(check_all)
x = 1
for y in check_all:
    x *= y
    print(x)
