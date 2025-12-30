Introduction

The DoS & DDoS Attack Simulation with Mitigation System is a Python‑based cybersecurity project that demonstrates how different types of network attacks can be simulated and how a defensive system can detect, log, and respond to these attacks in real time.
This project provides a practical understanding of networking, multithreading, socket programming, and security monitoring.

🎯 Objectives

The main objectives of this project are:

Simulate common cyber attacks such as DoS, DDoS, SYN Flood, SQL Injection, and UDP Flood

Design a real‑time mitigation system that detects and logs attacks

Understand client–server communication using socket programming

Develop user‑friendly GUI applications using Tkinter

Demonstrate the use of multithreading for concurrent operations

🖥️ System Requirements
Hardware Requirements
Component	Requirement
Processor	1 GHz or faster
RAM	2 GB minimum
Hard Disk	500 MB free space
Software Requirements

Python 3.9 or higher

Windows OS (Recommended)

Required Libraries

Install required library using:

pip install pillow

Standard Libraries Used

socket, threading, datetime, tkinter, os, subprocess, platform

Summary of Library Roles
Library	Purpose
socket	Network communication
threading	Parallel execution
tkinter	GUI development
datetime	Time & date logging
os	File management
subprocess	IP scanning
pillow	Custom GUI graphics
🏗️ System Design
Architecture

This project follows the Client–Server Model.

🧨 Attacker (Client)

Generates simulated attacks

Scans network IP addresses

Provides attack control interface

🛡️ Mitigator (Server)

Listens on port 9999

Detects incoming attacks

Logs and displays attack information

Generates downloadable reports

Workflow

Start the Mitigator server

Attacker scans the local network

User selects attack type

Attacker sends attack signal

Mitigator logs and displays the attack

✨ Features
🧨 Attacker Application

GUI‑based control panel

Supports multiple attack types

Network IP scanner

Multi‑threaded ping scanning

Saves previous IP for reuse

Clean modern interface

🛡️ Mitigator Application

Real‑time attack detection

Live attack monitoring

Automatic log file generation

Downloadable reports

Scrollable attack history

Auto‑start server option

🧪 Testing
Test Case	Expected Outcome	Result
Server startup	Server starts correctly	✅ Pass
Attack transmission	Attack delivered to Mitigator	✅ Pass
Log generation	Logs recorded properly	✅ Pass
GUI update	Logs displayed in real time	✅ Pass
File saving	Logs saved to Desktop	✅ Pass
Multithreading	Stable concurrent operation	✅ Pass
📜 Sample Attack Log
NEW ATTACK DETECTED!

Attack Type: DDoS
Attacker IP: 192.168.1.10
Attacker Port: 53241
Time of Attack: 14:32:11
Day of Attack: Monday, 30 December 2025
Action Taken: Action taken against attacker 192.168.1.10 ...

🎓 Learning Outcomes

This project helps in understanding:

Network attack behavior

Client–server communication

Socket programming

Multithreading concepts

GUI development

Logging and monitoring systems

Cybersecurity defense mechanisms

🚀 Future Enhancements

Authentication system

Encrypted communication

Real‑time traffic analysis

AI‑based detection system

Web‑based monitoring dashboard

🧾 Conclusion

This project demonstrates how network attacks can be simulated and how an effective mitigation system can detect, log, and respond to them.
It serves as a complete academic cybersecurity project integrating networking, security, and software development.

⚠️ Disclaimer

This project is strictly for academic and educational purposes.
It must not be used on real networks without proper authorization.

👨‍💻 Author

Nayyab Gul
Cybersecurity & Software Engineering Project
