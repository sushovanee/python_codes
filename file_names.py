import os
thisdir = os.getcwd()
print(thisdir)
# path = 'C:\\Users\\SP046767\\OneDrive - Cerner Corporation\Personal\\projects\\python'
for root, dirs, files in os.walk(thisdir):
    for filename in files:
        print(filename)