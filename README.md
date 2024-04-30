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
    |-- downloader.py
    |-- flow_pcap.py
    |-- Model 
        |-- ResNet.py
        |-- model.py
        |-- run.py
    |-- PEdeleter.py
    |-- Pcap2Img.py
    |-- tempDeleter.py
    |-- uploader.py
    |-- README.md
```

By **[Benson](https://github.com/benson5104)**
  - **uploader.py**: Uploads viruses to the api server of cuckoo sandbox, be sure to change the result to the place you want to .pcap files to be and change PEs to the folder containing viruses, also              change api token to your own token in cuckoo.conf
  
  - **downloader.py**: Downloads .pcap file from the api server, be sure to change the result folder and api token to your own token
  
  - **tempdeleter.py**: only used when the vmware goes down, deletes all other folders in result if the api token is larger than number in line20(line>=3920)
  
  - **PEdeleter.py**: only used when vmware goes down, run it after tempdeleter, it will remove all files that are already processed

By **[RayminQAQ](https://github.com/RayminQAQ)**:
  - Files in "**Model**" folder: Whole Machine Learning pipline for training and testing.
  - **flow_pcap.py**: split pcap into small pieces (seperated by TCP) according to the paper.

## Pipeline
The project is run in Python 3.8.10 and cuda version 12.3 (RTX 3060 laptop).

To setup the environment, you should setup python's virtual environment and type:

1. run the uploader.py to upload the files to api server
    (Notice: You should change your apikey)
    ```shell
    python uploader.py
    ```

2. run the downloader.py after all the files are processed to download all .pcap files
  (WARNING: you may come into many problem due to the setting of cuckoo sandbox, see [cuckoo sandbox documentation](https://cuckoo.readthedocs.io/en/latest/) for help.)

    ```shell
    python downloader.py
    ```

4. Turn pcap file into image (.png)

    ```shell
    python flow_pcap.py
    python Pcap2Img.py
    ```
    
5. Train the Maching Learning model
    ```shell
    python run.py
    ```

## Referece Paper
![](https://github.com/RayminQAQ/pcap_MalDetect/blob/main/image.png?raw=true)

1. [Malware Traffic Classification Using Convolutional
Neural Network for Representation Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7899588)
2. [Image-based Neural Network Models for Malware Traffic
Classification using PCAP to Picture Conversion
](https://dl.acm.org/doi/pdf/10.1145/3538969.3544473)

# Contributors
1. **[RayminQAQ](https://github.com/RayminQAQ)**:
    - In the repository: Processed pcap files according to the referenced paper and built the entire machine learning pipeline.
    - In the team: Supervised everyone's tasks and lead the team.
2. **[Stan Wang](https://github.com/StanNTUST)**:
3. **[Benson](https://github.com/benson5104)**: I made uploader.py, downloader.py, tempdeleter.py and PEdeleter.py
