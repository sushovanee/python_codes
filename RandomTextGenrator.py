import random
import string
import time
# from datetime import datetime
#
#  now = datetime.now()
#  current_time = now.strftime("%H:%M:%S")

def fun(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

for i in range(10):
    print (fun(20), time.strftime("%c") )
    time.sleep(2)
