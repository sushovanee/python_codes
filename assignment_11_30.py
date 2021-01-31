import re
given_list = ['mallika_1.jpg', 'dog005.jpg', 'grandson_2018_01_01.png', 'dog008.jpg', 'mallika_6.jpg', 'grandson_2018_5_23.png', 'dog01.png', 'mallika_11.jpg', 'mallika2.jpg', 'grandson_2018_02_5.png', 'grandson_2019_08_23.jpg', 'dog9.jpg', 'mallika05.jpg']

def ordinary_sorting(input_list): 
    """ Sort the given iterable in the way that ordinary people expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(input_list, key = alphanum_key)

def main():
    s = set(given_list)
    for x in ordinary_sorting(s):
        print(x)

if __name__ == '__main__':
    main()