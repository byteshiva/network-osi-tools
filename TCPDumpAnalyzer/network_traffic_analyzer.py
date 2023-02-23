import pandas as pd
from scapy.all import *

# Function to extract relevant information from captured packet
def packet_info(packet):
    return {
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "protocol": packet[IP].proto,
        "length": len(packet),
    }

# Capture TCP Dump data
packets = sniff(filter="tcp", count=100)

# Extract relevant information from captured packets
packet_data = [packet_info(packet) for packet in packets]

# Create pandas DataFrame from packet data
df = pd.DataFrame(packet_data)

# Display source and destination IP addresses
print("Source IPs:", df["src_ip"].unique())
print("Destination IPs:", df["dst_ip"].unique())
