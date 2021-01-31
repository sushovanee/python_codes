import random
from collections import Counter


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    out_put = rand7()
    if out_put <= 5:
        return out_put
    else:
        rand5()

test_list = []
for _ in range(100):
    # print('Rolling 5-sided die...')
    # print(rand5())
    test_list.append(rand5())
    
# print(test_list)
print(Counter(test_list))  

class Car():
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
audi = Car('red', 100)
print(audi.color)
print(audi.speed)