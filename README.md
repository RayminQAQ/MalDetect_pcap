# Project name: pcap_MalDetect
## Purpose: 
Created in 2024/3/17, using 
  1. cuckoo sandbox to generate pcap from malware
  2. malware dataset from VirusShare.com (orginate in VirusShare_00177).
  > VirusShare_00177 Dataset Overview:
>   
  > The VirusShare_00177 dataset is a collection of malware samples that were submitted to the VirusShare website. The dataset includes both benign and malicious     samples, and it can be used for a variety of machine learning tasks, such as malware detection and classification.

## Project Structure

```
Repository file structure:
    |-- Model 
        |-- ResNet.py
        |-- model.py
        |-- run.py
    |-- PEdeleter.py
    |-- Pcap2Img.py
    |-- downloader.py
    |-- downloader.py
    |-- README.md
```

By **[Benson](https://github.com/benson5104)**
- uploader.py: Uploads viruses to the api server of cuckoo sandbox, be sure to change the result to the place you want to .pcap files to be and change PEs to the folder containing viruses, also              change api token to your own token in cuckoo.conf

- downloader.py: Downloads .pcap file from the api server, be sure to change the result folder and api token to your own token

- tempdeleter.py: only used when the vmware goes down, deletes all other folders in result if the api token is larger than number in line20(line>=3920)

- PEdeleter.py: only used when vmware goes down, run it after tempdeleter, it will remove all files that are already processed

By **[RayminQAQ](https://github.com/RayminQAQ)**:
- Model directory:
- Pcap2Img.py:

## Pipeline
The project is run in Python 3.8.10 and cuda version 12.3 (RTX 3060 laptop), package dependencies are stored in requirement.txt.

To setup the environment, you should setup python's virtual environment and type:
```shell
python requirement.txt
```
1. run the uploader.py to upload the files to api server
    ```shell
    python uploader.py
    ```

2. run the downloader.py after all the files are processed to download all .pcap files
3. 
(WARNING: you may come into many problem due to the setting of cuckoo sandbox, see [cuckoo sandbox documentation](https://cuckoo.readthedocs.io/en/latest/) for help.)
    ```shell
    python downloader.py
    ```

4. tmp



## Referece Paper


# Contributors
1. **[RayminQAQ](https://github.com/RayminQAQ)**:
  - In the repository: Processed pcap files according to the referenced paper and built the entire machine learning pipeline.
  - In the team: Supervised tasks and lead the whole team.
2. Stan Wang:
3. **[Benson](https://github.com/benson5104)**: I made uploader,downloader,tempdeleter and PEdeleter
