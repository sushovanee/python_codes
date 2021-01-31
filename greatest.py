def largest_num(in_list):
    large_num = 0
    for i in in_list:
        if i > large_num:
            large_num = i
    print(large_num)

check_list = [2,3,5,1,3,9,9,111]
largest_num(check_list)
