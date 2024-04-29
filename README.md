# Project name: pcap_MalDetect
Created in 2024/3/17, using cuckoo sandbox to generate pcap from malware, and malware from VirusShare.com (orginate in VirusShare_00177).

# Referece Paper: 
1. 

# Contributors
1. RayminQAQ
2. Stan Wang
3. Benson

# VirusShare_00177 Dataset README

This README file provides information about the VirusShare_00177 dataset and how to use it.

## Dataset Overview

The VirusShare_00177 dataset is a collection of malware samples that were submitted to the VirusShare website. The dataset includes both benign and malicious samples, and it can be used for a variety of machine learning tasks, such as malware detection and classification.

## Dataset Structure

The dataset is organized into the following folders:

* **all:** This folder contains all of the raw data files.
* **train:** This folder contains the training data.
* **validate:** This folder contains the validation data.
* **test:** This folder contains the test data.
* **doc:** This folder contains documentation for the dataset.
* **models:** This folder contains trained models.
* **data:** This folder contains processed data.

Each of the train, validate, and test folders contains the following subfolders:

* **img:** This folder contains images of the malware samples.
* **api:** This folder contains API calls made by the malware samples.

Each of the img and api folders contains the following files:

* **api.npy:** This file contains a NumPy array of API calls.
* **img.npy:** This file contains a NumPy array of images.
* **idx_mapping.json:** This file contains a JSON mapping from indices to malware samples.
* **seq_length.json:** This file contains a JSON mapping from malware samples to sequence lengths.

The doc folder contains the following files:

* **README.md:** This file contains the dataset README.
* **license.txt:** This file contains the dataset license.
