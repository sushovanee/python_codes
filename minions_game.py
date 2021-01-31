
def minion_game(string):
    # your code goes here
    string_list = []
    all_strings = []
    string_list[:0]=string 
    # string_list = string.split('')
    # print(string_list)
    for i in range(len(string_list)):
        for j in range(len(string_list)):
            if j >= i:
                char = ''.join(string_list[i:j+1])
                # print(char)
                all_strings.append(char)
    # print(all_strings)
    all_strings_count = {}
    for entry in all_strings:
        if entry in all_strings_count.keys():
            all_strings_count[entry] += 1
        else:
            all_strings_count[entry] = 1
            
    return all_strings_count
    
def vowel_consonent(all_strings_count):
    the_vowel = ["a","e","i","o","u"]
    vowel_dict = {}
    cons_dict = {}
    for entry in all_strings_count.keys():
        if entry[0].lower() in the_vowel:
            vowel_dict[entry] = all_strings_count[entry]
        else:
            cons_dict[entry] = all_strings_count[entry]
    print(vowel_dict)
    print(sum(vowel_dict.values()))
    print('---------------------------------------------')
    print(cons_dict)
    print(sum(cons_dict.values()))

def minion_game_simplified(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
            print(string[i], K)
        else:
            S+=len(string)-i
            print(string[i], S)
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game_simplified(s)