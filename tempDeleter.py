import requests
import os
import time
import shutil

destination_path = "/home/nigger/下載/virushare-20/result/"
header = {"Authorization": "Bearer IgGzFFa705J0Nm2BlwRyRQ"}

allFolders = os.listdir(destination_path)

for folders in allFolders:
    api_name = os.path.join(destination_path, folders,"apiKeys.txt")
    api = open(api_name,'r')
    task_id = api.readlines()
    print (folders)
    for idx,line in enumerate(task_id):
        line = line.strip()
        task_id[idx] = int(line)
    for idx,line in enumerate(task_id):
        if(line >=3920):
            shutil.rmtree((os.path.join(destination_path,folders)))
            break
        #print(line)
    #os.remove(api_name)
