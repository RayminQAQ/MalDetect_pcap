#used to download files uploaded to api server

import requests
import os

destination_path = "/home/nigger/下載/virushare-20/result/"
header = {"Authorization": "Bearer IgGzFFa705J0Nm2BlwRyRQ"}

allFolders = os.listdir(destination_path)

for folders in allFolders:
    api_name = os.path.join(destination_path, folders,"apiKeys.txt")
    api = open(api_name,'r')
    task_id = api.readlines()
    for idx,line in enumerate(task_id):
        line = line.strip()
        task_id[idx] = int(line)
    for idx,line in enumerate(task_id):
        result_url = f"http://localhost:8090/pcap/get/{line}"
        result = requests.get(result_url, headers=header)
        with open(os.path.join(destination_path,folders,str(line)+".pcap"), "wb") as f:
            f.write(result.content)
    #os.remove(api_name)
