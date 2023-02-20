#!/usr/bin/env python

from scapy.all import *
import argparse

results = {}

def tcp_scan(host, port):
    src_port = RandShort()
    tcp_connect_scan_resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0)
    if tcp_connect_scan_resp is not None:
        if tcp_connect_scan_resp.haslayer(TCP):
            if tcp_connect_scan_resp[TCP].flags == 0x12:
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=port,flags="R"),timeout=1,verbose=0)
                print(f"Port {port} is open.")
                results[port] = "open"
            elif tcp_connect_scan_resp[TCP].flags == 0x14:
                print(f"Port {port} is closed.")
                results[port] = "closed"
        else:
            print(f"Port {port} is filtered.")
            results[port] = "filtered"

def tcp_scan_cached(host, ports):
    for port in ports:
        if port in results:
            if results[port] == "open":
                print(f"Port {port} is open. (cached)")
            elif results[port] == "closed":
                print(f"Port {port} is closed. (cached)")
            else:
                print(f"Port {port} is filtered. (cached)")
        else:
            tcp_scan(host, port)

def main():
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("host", help="Target IP address or hostname.")
    parser.add_argument("ports", nargs="+", type=int, help="Space separated list of ports to scan.")
    args = parser.parse_args()

    host = args.host
    ports = args.ports

    tcp_scan_cached(host, ports)

if __name__ == "__main__":
    main()
