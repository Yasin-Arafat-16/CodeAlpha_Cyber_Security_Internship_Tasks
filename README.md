# Network Intrusion Detection System (NIDS) - CodeAlpha

This project is a Python-based Network Intrusion Detection System (NIDS) developed as part of my Cyber Security internship at CodeAlpha.

## Features
- **SYN Flood Detection:** Detects excessive SYN packets to prevent DoS attacks.
- **Port Scanning Detection:** Identifies IPs scanning multiple ports within a short time.
- **Malicious Payload Detection:** Monitors for suspicious keywords like 'admin', 'sql', 'passwd' in network traffic.
- **Real-time Logging:** Saves all alerts with severity levels in a log file.

## Technologies Used
- Python 3.x
- Scapy (Network Packet Manipulation)

## How to Run
1. Install Scapy: `pip install scapy`
2. Run as Administrator: `python Final_NIDS_Project.py`
