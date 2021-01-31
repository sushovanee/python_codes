# Enter your code here. Read input from STDIN. Print output to STDOUT
def cal_mean(ip_list):
    sum_list = 0
    if len(ip_list) > 0:
        for entry in ip_list:
            sum_list += entry
    else:
        sum_list = entry
    
    return (sum_list/len(ip_list))

def cal_median(ip_list):
    if len(ip_list)%2 == 0:
        return int(sum(ip_list[len(ip_list)//2-1:len(ip_list)//2+1])/2)
    else:
        return ip_list[len(ip_list)//2]

def cal_mode(ip_list):
    count_dict = {}
    for entry in ip_list:
        if entry in count_dict.keys():
            count_dict[entry] += 1
        else:
            count_dict[entry] = 1
    return max(count_dict, key=count_dict.get)

def cal_weight_mean(num_list, wght_list):
    """
    This function calculates weighted sum of an array
    WM = sum(x*w)/sum(w)
    """
    wght_sum = 0
    denominator_sum = 0
    if len(num_list) == len(wght_list):
        for i in range(len(num_list)):
            wght_sum += (num_list[i] * wght_list[i])
            denominator_sum += wght_list[i]
        return (wght_sum/denominator_sum)
    else:
        return None

def quantile_cut(ip_list):
    ip_list.sort()
    lower_list = []
    upper_list = []
    if (len(ip_list)%2 == 0):
        for i in range(0, (len(ip_list)/2)):
            lower_list.append(ip_list[i])
        for j in range(len(ip_list)/2, len(ip_list)):
            upper_list.append(ip_list[j])
    else:
        for i in range(0, int(len(ip_list)/2)):
            lower_list.append(ip_list[i])
        for j in range(int(len(ip_list)/2)+1, len(ip_list)):
            upper_list.append(ip_list[j])
    return lower_list, upper_list


def main():
    input_count = int(input('Enter input count: '))
    # for hackerank submission
    # ip_list = list(map(int, input().split()))
    # ip_list = []
    # for i in range(input_count):
    #     ip_list.append(int(input()))
    # list_mean = cal_mean(ip_list)
    # print('Mean: ', list_mean)
    # list_median = cal_median(ip_list)
    # print('Median', list_median)
    # list_mode = cal_mode(ip_list)
    # print('Mode: ', list_mode)
    # input_count = int(input())
    ip_list = []
    for i in range(input_count):
        ip_list.append(int(input()))
    Q2 = cal_median(ip_list)
    lower_list, upper_list = quantile_cut(ip_list)
    print(lower_list)
    print(upper_list)
    Q1 = cal_median(lower_list)
    Q3 = cal_median(upper_list)
    print(Q1)
    print(Q2)
    print(Q3)

if __name__ == "__main__":
    main()


    
    
