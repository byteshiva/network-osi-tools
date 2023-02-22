import pandas as pd
from scapy.all import rdpcap

# Load the pcap file into a list of packets
packets = rdpcap("traffic.pcap")

# Initialize a list to hold packet details
packet_details = []

# Extract packet details and append to the list
for packet in packets:
    packet_dict = {
        'src': None,
        'dst': None,
        'proto': None,
        'length': None,
        'time': None
    }
    if packet.haslayer('IP'):
        packet_dict['src'] = packet['IP'].src
        packet_dict['dst'] = packet['IP'].dst
        packet_dict['proto'] = packet['IP'].proto
        packet_dict['length'] = packet['IP'].len
        packet_dict['time'] = packet.time
    packet_details.append(packet_dict)

# Convert the list of packets to a Pandas dataframe
df = pd.DataFrame(packet_details)

# Group packets by source IP and protocol, and calculate statistics
grouped = df.groupby(['src', 'proto']).agg({'length': ['count', 'mean', 'std', 'min', 'max']})
print(grouped)
