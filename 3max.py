''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

# def main():

 # # Write code here 
 # a = int(input())
 # b = int(input())
 # c = int(input())
 # if a>b:
    # if a>c:
         # print('largest:' + str(a),end="")
    # else:
            # print('largest:' + str(c),end="")
 # else:
        # if b>c:
            # print('largest:' + str(b),end="")
        # else:
            # print('largest:' + str(c),end="")

def main():
    temp_list = []
    temp_size = int(input('enter size: '))
    for i in range(temp_size):
        temp_list.append(int(input()))
    print('max is: ' + str(max(temp_list)))

main()