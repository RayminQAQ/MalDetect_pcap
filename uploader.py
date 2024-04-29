#used to upload viruses to api server

import requests
import os

url = "http://localhost:8090/tasks/create/file"
file = "/home/nigger/下載/virushare-20/PE2s/"
destination_path = "/home/nigger/下載/virushare-20/result/"
header = {"Authorization": "Bearer IgGzFFa705J0Nm2BlwRyRQ"}

allFiles = os.listdir(file)
for folder in allFiles:  #list all folders
    if not os.path.exists(os.path.join(destination_path, folder)):
        os.mkdir(os.path.join(destination_path, folder))
    f = open(os.path.join(destination_path, folder, "apiKeys.txt"), "w")
    filenames = os.listdir(os.path.join(file, folder))

    for filename in filenames:  #list all files in folder
        with open(os.path.join(file, folder, filename), "rb") as file_in_folder:
            files = {"file" : ("temp_file_namae", file_in_folder)}
            r = requests.post(url, headers=header, files=files)
            f.write(str(r.json()["task_id"])+"\n")