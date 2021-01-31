def gen_prime_num(start_num, end_num):
    prime_num_list = []
    for i in range(start_num, end_num):
        factor_count = 0
        for j in range(2,i):
            if i%j==0:
                factor_count += 1
            # else:
            #     factor_count += 1
            #     prime_num_list.append(i)
        if factor_count == 0:
            prime_num_list.append(i)
    return prime_num_list

def main():
    start_num = int(input('Enter starting number: '))
    end_num = int(input('Enter ending number: '))
    print('Your prime numbers are... ')
    check_list = gen_prime_num(start_num,end_num)
    print(check_list)

if __name__ == '__main__':
    main()