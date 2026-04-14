# CodeAlpha Cyber Security Internship Tasks

This repository contains the completed tasks for my Cyber Security internship at **CodeAlpha**. These projects demonstrate hands-on experience in network traffic analysis and threat detection.

## 📋 Projects Overview

### 1. Basic Network Sniffer (Task 01)
A Python-based tool developed to capture and analyze network traffic.
- **Functionality:** Identifies protocols like TCP, UDP, and ICMP.
- **Credential Detection:** Monitors for unencrypted login data (username/password) in HTTP traffic.
- **File Name:** `Cybersecurity Internship Task-01.py`.

### 2. Network Intrusion Detection System - NIDS (Task 04)
An advanced monitoring system designed to detect and alert against potential network threats.
- **Detection Capabilities:**
    - **SYN Flood:** Detects potential Denial of Service (DoS) attempts.
    - **Port Scanning:** Identifies suspicious scanning of multiple ports.
    - **Malicious Payload:** Flags packets containing sensitive keywords like 'admin' or 'sql'.
- **Response Mechanism:** Generates real-time alerts and maintains a log file (`nids_alerts.log`) for incident analysis.
- **File Name:** `Cybersecurity Internship Task-04.py`.

---

## 🛠️ Setup & Requirements

### Prerequisites
Make sure you have Python 3.x installed along with the `scapy` library:
```bash
pip install scapy
