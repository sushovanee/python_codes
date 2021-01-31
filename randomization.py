import numpy as np
np.random.seed(123)

tails = [0]

for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)
    print("x is: " + str(x))
    print("coin toss is: " + str(coin))
    print("tail is: " + str(tails[x]))

print(tails)
