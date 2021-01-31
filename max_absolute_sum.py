
def max_abs_sub_sum(input_array):
    abs_array = []
    for entry in input_array:
        if entry < 0:
            abs_array.append(-1*entry)
        else:
            abs_array.append(entry)
    abs_array = sorted(abs_array, reverse=True)
    print(abs_array)
    return (abs_array[0]+abs_array[1])

    
if __name__ == '__main__':
    input_array = [4, -6, 2, -7, 5, 4]
    print(max_abs_sub_sum(input_array))