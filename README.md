DoS & DDoS Attack Simulation with Mitigation System
🎯 Purpose

This project demonstrates how common cyber attacks can be simulated and how a mitigation system can detect, log, and respond to them in real time.
It is developed strictly for educational and academic purposes to help understand practical cybersecurity concepts.

📌 Project Overview

This project consists of two major components:

Component	Description
ATTACKER	Simulates multiple types of cyber attacks and performs LAN device scanning
MITIGATOR	Acts as a defensive system that detects attacks, records detailed logs, and generates downloadable reports

Both components are built using Python, Tkinter GUI, Socket Programming, Multithreading, and File Logging.

🧩 Features
🧨 Attacker Application

GUI-based control panel

Attack types supported:

DoS

DDoS

SYN Flood

SQL Injection

UDP Flood

Network IP Scanner

Multi-threaded ping scanning

Stores previous target IP for quick reuse

Clean modern UI with rounded buttons

🛡️ Mitigator Application

Real-time server listening on port 9999

Automatically detects incoming attacks

Displays:

Attack type

Attacker IP & port

Date & time

Action taken

Saves logs to Desktop

Downloadable log reports

Scrollable GUI log monitor

Can auto-start server on launch (server-less version)

🖥️ System Requirements

Python 3.9+

Windows OS (Recommended)

📦 Required Libraries
pip install pillow


Standard libraries used:
socket, threading, datetime, tkinter, os, subprocess, platform

🚀 How to Run
1️⃣ Start the Mitigator
python mitigator.py


If using WITHOUT SERVER version, the server starts automatically.

2️⃣ Start the Attacker
python attacker.py

3️⃣ Simulation Flow

Launch Mitigator

Launch Attacker

Click Scan IP

Choose an Attack Type

Enter Target IP

Send Attack

Watch logs appear live in Mitigator

🧪 Attack Log Example
NEW ATTACK DETECTED!
--------------------------------------------------
Attack Type: DDoS
Attacker IP: 192.168.1.10
Attacker Port: 53241
Time of Attack: 14:32:11
Day of Attack: Monday, 30 December 2025
--------------------------------------------------
Action Taken: Action taken against attacker 192.168.1.10 ...
--------------------------------------------------

📁 Log Files

Automatically saved to the Desktop

Example filename:

MITIGATOR_LOG_20251230_143211.txt

🧠 Learning Outcomes

This project strengthens understanding of:

Network attacks and their impact

Client-server communication

Socket programming

Multithreading

GUI development

Logging & reporting systems

Cybersecurity simulation and defense mechanisms

⚠️ Disclaimer

This software is created only for academic and learning purposes.
It must not be used on real networks or systems without proper authorization.

👨‍💻 Author

Nayyab Gul
Cybersecurity & Software Engineering Project
