import os
import shutil

destination_path = "/home/nigger/下載/virushare-20/result/"
header = {"Authorization": "Bearer IgGzFFa705J0Nm2BlwRyRQ"}
PEs  = "/home/nigger/下載/virushare-20/PEs/"
allFolders = os.listdir(destination_path)

for folders in allFolders:
    print(folders)
    shutil.rmtree(os.path.join(PEs,folders))
        #print(line)
    #os.remove(api_name)
