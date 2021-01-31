# from googletrans import Translator

# translator = Translator()

# l1 = translator.translate('안녕하세요.')
# print(l1.text)

# l2 = translator.translate('안녕하세요.', dest='bn')
# print(l2.text)

# l3 = translator.translate('veritas lux mea', src='la')
# print(l3.text)

# l = [1,2,3,4]
# l = ''.join(str(entry) for entry in l)
# print(int(l)+1)
# l = str(l)
# l = l.split('')
# print(l)

def isPrime(n):
    # Write your code here
    if n > 2:
        for i in range(2,n):
            if (n%i)==0:
                return i
            else:
                return 1
    else:
        return 1
        
        
if __name__ == '__main__':
    n = int(input())
    ans = isPrime(n)
    print(ans)
    
    
# AECPP5942G