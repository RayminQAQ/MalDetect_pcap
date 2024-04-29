# -- coding: utf-8 --
"""
Created on Mon Apr 29 10:57:47 2024

@author: Stan Wang
"""

import os
import numpy as np
from PIL import Image

pcap_data_path="result_Pcap/"
image_data_path="image_data/"
def pcapToHexbyte(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        hex_data = binary_data.hex()

    byte_length = len(hex_data) // 2
    if byte_length > 784 :
        hex_data = hex_data[:1568]
    elif byte_length < 784 :
        hex_data += '00' * (784  - byte_length)

    return hex_data

def HexbyteToImage(hex_data,path,name):
    if not os.path.exists(path):
        os.makedirs(path)
    byte_array = bytes.fromhex(hex_data)
    img_data = np.array(list(byte_array), dtype=np.uint8).reshape(28, 28)
    img = Image.fromarray(img_data, 'L')  # 'L' 代表灰階模式
    full_path = path+"/"+name[:-5]+".png"
    img.save(full_path)

catagoryPath= os.listdir(pcap_data_path)
catagoryTotalNumber=len(catagoryPath)
for counter, name in enumerate(catagoryPath):
    tempPath = pcap_data_path+name+"/"
    tmpData= os.listdir(tempPath)
    tmpTotalNumber=len(tmpData)
    for counter2, tmpName in enumerate(tmpData):
        pcapPath= tempPath+tmpName+"/"
        pcapData= os.listdir(pcapPath)
        pcapTotalNumber=len(tmpData)
        for counter3, pcapName in enumerate(pcapData):
            hex_data=pcapToHexbyte(pcapPath+pcapName)
            image=HexbyteToImage(hex_data,image_data_path+name,pcapName)
            print(counter+1,"/",catagoryTotalNumber," catogory, ",counter2+1,"/",tmpTotalNumber," tmpPath, ",counter3+1,"/",pcapTotalNumber," pcapFile",sep="")