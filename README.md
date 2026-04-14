Basic Network Sniffer - CodeAlpha Task 1
This is a professional Python-based Network Sniffer developed as part of my Cyber Security internship at CodeAlpha. The tool captures and analyzes real-time network traffic, identifying various protocols and extracting potential login credentials from unencrypted HTTP traffic.

🚀 Features
Multi-Protocol Support: Captures and identifies TCP, UDP, and ICMP packets.

Credential Detection: Automatically monitors for sensitive keywords (username, password, email, etc.) in unencrypted (HTTP) data.

Formatted Table View: Displays network traffic in a clean, organized table format including timestamp, IPs, and ports.

Real-time Alerting: Highlights critical events when login data is detected.

Payload Summary: Provides a brief overview of the raw data transmitted in each packet.

🛠️ Technologies Used
Python 3.x

Scapy: A powerful Python-based interactive packet manipulation program and library.

📋 Prerequisites
To run this tool, you need to have Python and Scapy installed on your system.

Install Scapy:

Npcp/WinPcap (Windows Users):
Ensure you have Npcap or WinPcap installed for Scapy to capture packets correctly on Windows.

💻 How to Use
Clone this repository or download the source code.

Open your terminal or Command Prompt as Administrator.

Run the script:

To test credential detection, visit an unencrypted (HTTP) login page (e.g., ) and try to log in.

📸 Output Preview
The tool generates a live table of network traffic:

When credentials are found, it triggers a critical alert:

⚠️ Disclaimer
This tool is for educational and ethical purposes only. Monitoring network traffic without permission is illegal and unethical. Use this tool only on networks you own or have explicit permission to test.

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
