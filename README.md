Basic Port Scanner

Project Overview

This project is a basic port scanner written in Python. It allows users to scan a range of ports on a given host to determine whether they are open or closed. This tool is useful for network administrators, cybersecurity professionals, or anyone interested in assessing the security of a system or network by identifying exposed ports.

Features

Scan Range of Ports: Scan any specified range of ports on a given target host.

Multithreaded: Uses Python's threading capabilities for faster scanning of multiple ports simultaneously.

Customizable: Easily extendable to add more features like service detection, banner grabbing, etc.

Command-Line Interface (CLI): Simple to use through the command line.


Requirements

To run this project, you need:

Python 3.x (Recommended)

Socket library (Built-in Python library)


Installation

1. Clone the repository to your local machine:

git clone https://github.com/yourusername/basic-port-scanner.git


2. Navigate to the project directory:

cd basic-port-scanner


3. No additional dependencies are required as the script uses the built-in socket library in Python.



Usage

1. Open a terminal in the project directory and run the port scanner:

python port_scanner.py <target_host> <start_port> <end_port>

<target_host>: The IP address or domain name of the target system.

<start_port>: The first port in the range to scan.

<end_port>: The last port in the range to scan.


Example:

python port_scanner.py 192.168.1.1 1 1024

This will scan ports 1 through 1024 on the target IP 192.168.1.1.


2. The script will display which ports are open and closed during the scan.



Contribution

Feel free to fork this repository and submit pull requests for any improvements or fixes. Contributions are welcome!
