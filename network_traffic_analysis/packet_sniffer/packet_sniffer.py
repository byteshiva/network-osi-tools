from collections import defaultdict
from scapy.all import *

def process_packet(packet, stats):
    proto = packet[IP].proto
    if proto not in stats['packets_by_protocol']:
        stats['packets_by_protocol'][proto] = 0
    stats['packets_by_protocol'][proto] += 1

    src = packet[IP].src
    if src not in stats['packets_by_src_ip']:
        stats['packets_by_src_ip'][src] = 0
    stats['packets_by_src_ip'][src] += 1

def print_stats(stats):
    print('---Packet Statistics---')
    for proto, count in stats['packets_by_protocol'].items():
        print(f"Protocol {proto}: {count} packets")
    for ip, count in stats['packets_by_src_ip'].items():
        print(f"Source IP {ip}: {count} packets")

def main():
    stats = defaultdict(lambda: 0, {'packets_by_protocol': {}, 'packets_by_src_ip': {}})
    filter_packets = 'ip'
    packets = sniff(filter=filter_packets, prn=lambda x: process_packet(x, stats))
    print_stats(stats)

if __name__ == '__main__':
    main()
