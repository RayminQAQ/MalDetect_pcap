# Project name: pcap_MalDetect
## Purpose: 
Created in 2024/3/17, using 
  1. cuckoo sandbox to generate pcap from malware
  2. malware dataset from VirusShare.com (orginate in VirusShare_00177).
  > VirusShare_00177 Dataset Overview:
>   
  > The VirusShare_00177 dataset is a collection of malware samples that were submitted to the VirusShare website. The dataset includes both benign and malicious     samples, and it can be used for a variety of machine learning tasks, such as malware detection and classification.

## Project Structure
uploader: Uploads viruses to the api server of cuckoo sandbox, be sure to change the result to the place you want to .pcap files to be and change PEs to the folder containing viruses, also              change api token to your own token in cuckoo.conf

downloader: Downloads .pcap file from the api server, be sure to change the result folder and api token to your own token

tempdeleter: only used when the vmware goes down, deletes all other folders in result if the api token is larger than number in line20(line>=3920)

PEdeleter: only used when vmware goes down, run it after tempdeleter, it will remove all files that are already processed


## Pipeline
The project is run in Python 3.8.10 and cuda version 12.3 (RTX 3060 laptop), package dependencies are stored in requirement.txt.

To setup the environment, you should setup python's virtual environment and type:
```shell
python requirement.txt.
```
1. run the uploader.py to upload the files to api server

2. run the downloader.py after all the files are processed to download all .pcap files
## Referece Paper


# Contributors
1. RayminQAQ
2. Stan Wang
3. Benson
