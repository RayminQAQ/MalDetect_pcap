#  -- coding: utf-8 --
"""
Created on Mon Apr 29 2024

@author: RayminQAQ
@Purpose: split pcap into small pieces (seperated by TCP)
"""

import os
import random
from scapy.all import *

def anonymize_ip(ip):
    # 將 IP 地址拆分成四個部分
    parts = ip.split('.')
    # 對每個部分進行隨機化處理
    anonymized_parts = [str(random.randint(0, 255)) for _ in range(4)]
    # 返回處理後的 IP 地址
    return '.'.join(anonymized_parts)


def save_unique_tcp_packets(pcap_file, output_dir):
    # Message
    print(f"Proccessing directory in {pcap_file}")

    # 使用 rdpcap 函數讀取 pcap 文件中的封包
    packets = rdpcap(pcap_file)

    # 使用集合來存儲已經見過的 TCP 封包摘要
    seen_packets = set()

    # 遍歷每個封包，過濾重複封包並保存到文件中
    for i, packet in enumerate(packets):
        if TCP in packet:
            # 如果封包摘要已經在集合中，跳過這個封包
            if packet.summary() in seen_packets:
                continue

            # 對源 IP 地址和目的 IP 地址進行亂數處理
            packet[IP].src = anonymize_ip(packet[IP].src)
            packet[IP].dst = anonymize_ip(packet[IP].dst)

            # 將封包摘要添加到已見封包集合中
            seen_packets.add(packet.summary())

            # 生成儲存文件名，使用時間戳和序號作為文件名的一部分
            filename = f"{output_dir}/tcp_packet_{packet.time}_{i}.pcap"
            wrpcap(filename, packet)


def createDir(path: str) -> None:
    if not os.path.isdir(path):
        os.mkdir(path)
    return

def main(input_dir: str, output_directory: str) -> None:
    createDir(output_directory)

    for folder in os.listdir(input_dir):
        createDir(f"{output_directory}/{folder}")

        for file in os.listdir(f"./{input_dir}/{folder}"):
            infile = f"{input_dir}/{folder}/{file}"
            outfile = f"{output_directory}/{folder}/{file}"

            if outfile.endswith(".pcap"):
                outfile = outfile[:-5]
            createDir(outfile)

            if "pcap" in file: # because the file would contain apiKeys.txt
                save_unique_tcp_packets(infile, outfile)


if __name__ == "__main__":
    # Modify
    input_dir = "./result"
    output_directory = "./result_Pcap"
    main(input_dir, output_directory)