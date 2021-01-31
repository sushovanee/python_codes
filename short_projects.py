def generate_acronym(user_input):
    text = user_input.split()
    a = " "
    for i in text:
        a = a+str(i[0]).upper()
    return a
    
def email_slicer():
    email = input("Enter Your Email: ").strip()
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
    print(format_)
    

if __name__ == '__main__':
    user_input = str(input("Enter a Phrase: "))
    acronym = generate_acronym(user_input)
    print(acronym)
    
    email_slicer()
    
def divide_equal_sum(in_list):
    list_cen = int(len(in_list)/2)
    l_sum = sum(in_list[:list_cen])
    r_sum = sum(in_list[list_cen+1:])
    while l_sum != r_sum:
        if l_sum > r_sum:
            list_cen -= 1
            l_sum = sum(in_list[:list_cen])
            r_sum = sum(in_list[list_cen+1:])
        else:
            list_cen += 1
            l_sum = sum(in_list[:list_cen])
            r_sum = sum(in_list[list_cen+1:])
    return list_cen
