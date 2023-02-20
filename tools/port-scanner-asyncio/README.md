# TCP Port Scanner

This is a simple TCP port scanner written in Python using the Scapy library.

## Usage
To run the scanner, execute the following command:

`
python tcp_port_scanner.py <target_ip> <port_range>
`

where `<target_ip>` is the IP address or hostname of the target, and `<port_range>` is a range of ports to scan, specified as a hyphen-separated pair of integers (e.g. `1-1024`).


## Output
The scanner will output a list of open, closed, and filtered ports for the target.

## Implementation
The scanner uses Scapy's sr1 and sr functions to send SYN and RST packets to the target's ports, and then interprets the responses to determine the status of each port.

## Installation 
To use Python Scapy with asyncio, you can install the scapy and asyncio-scapy packages.

Here are the installation and dependency steps for Python Scapy with asyncio:

## Install Scapy:

`
pip install scapy
`

## Install asyncio-scapy:


`
pip install asyncio-scapy
`

## Import Scapy and asyncio in your Python script:

```
from scapy.all import *
import asyncio
```
Make sure to use asyncio for event loop and use async and await for coroutines.

You may also need to install the following dependencies if they are not already installed:

- libpcap-dev or winpcap-dev for packet capturing
- pycrypto or cryptography for encrypted traffic capturing
The dependencies may vary depending on the operating system you are using.

That's it! You can now use Python Scapy with asyncio to build network scanning and packet analysis tools.





## Contributing
Contributions to this project are welcome. If you find a bug or would like to suggest a feature, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
