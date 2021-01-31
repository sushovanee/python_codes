# Program to show various ways to read and 
# write data in a file. 
import random
import os.path as pat
import os
import datetime
import glob


for i in range(10): 
    # L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
    filename = "myfile.txt"
    if (pat.exists(filename)):
        file1 = open(filename,"r+")
        last_index = int((file1.readlines()[-1:])[0])
        print("last number is: ", last_index)
        r1 = random.randint(0, 10)
        last_index += r1
        # \n is placed to indicate EOL (End of Line) 
        file1.writelines(str(last_index)+"\n") 
        # file1.writelines(L) 
        file1.close() #to change file access modes
    else:
        file1 = open(filename, "w")
        file1.writelines("1\n")
        file1.close()
     
now = datetime.datetime.now()
filename_string = now.strftime("%Y%m%d")
print(filename_string)

hiduu_data_path = 'C:/Users/SP046767/Downloads/Hiduu_process/bin/data/'
for file in glob.glob(hiduu_data_path + filename_string + '*.csv'):
    print(file)

file_list = sorted(glob.glob(hiduu_data_path + filename_string + '*.csv'))
print(file_list[-1])