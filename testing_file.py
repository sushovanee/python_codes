import timeit

# def mean_list(in_list):
#     sum=0
#     for entry in in_list:
#         sum = sum + entry
#     return (sum/len(in_list))

# print(mean_list([2,5,8,0,8,7]))

def read_file_text(filename):
    with open(filename, "r") as myfile: 
        data = myfile.read()
    return data

def reverse_string(string_text):
    return string_text[::-1]

# print(reverse_string('I want this text backward'))
def main():
    start = timeit.timeit()
    print('starting...')
    filename = "text_file.txt"
    reversed_string = reverse_string(read_file_text(filename))
    f1 = open("text_file.txt", "w")
    f1.write(reversed_string)
    end = timeit.timeit()
    print('time taken by program: ', end - start)

if __name__ == "__main__":
    main()
