#deleting duplicates from downloads
import os

path = 'C:/Users/91884/Downloads/'
items = os.listdir(path)
#print(len(items))
c = 0
total_size = 0
with os.scandir(path) as dir_contents:
    for entry in dir_contents:
        #print(entry)
        if '(1)' in str(entry):
            print(entry.name)
            c += 1
            size = entry.stat()
            total_size += size.st_size
            os.remove(path+str(entry.name))
print('-----------------------------------------')
print('Total items deleted:',c)
print('Total memory freed (in MB)',total_size/(1024**2))