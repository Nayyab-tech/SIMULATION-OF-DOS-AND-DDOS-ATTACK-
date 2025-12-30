# 🛡️ **DoS & DDoS Attack Simulation with Mitigation System**

---

## **1. _Introduction_**

The **DoS & DDoS Attack Simulation with Mitigation System** is a Python-based cybersecurity project that demonstrates how different types of network attacks can be simulated and how a defensive system can detect, log, and respond to these attacks in real time.  
This project provides practical understanding of **networking**, **multithreading**, **socket programming**, and **security monitoring**.

---

## **2. _Objective_**

The main objectives of this project are:

- To simulate common cyber attacks such as **DoS, DDoS, SYN Flood, SQL Injection, and UDP Flood**  
- To design a **real-time mitigation system** that detects and logs attacks  
- To understand **client-server communication** using socket programming  
- To develop user-friendly **GUI applications** using Tkinter  
- To demonstrate the use of **multithreading** for concurrent operations  

---

## **3. _System Requirements_**

### **_Hardware Requirements_**

| Component | Requirement |
|-----------|-------------|
| Processor | 1 GHz or faster |
| RAM       | 2 GB minimum |
| Hard Disk | 500 MB free space |

### **_Software Requirements_**

- **Python 3.9 or higher**  
- **Windows OS (Recommended)**  

### **_Required Libraries_**

Pillow library must be installed using:  
```bash
pip install pillow
### **_Standard Libraries Used_**
socket, threading, datetime, tkinter, os, subprocess, platform

### **_Summary of Library Roles_**

| Library    | Purpose                  |
|------------|-------------------------|
| socket     | Network communication    |
| threading  | Parallel execution       |
| tkinter    | GUI development          |
| datetime   | Time & date logging      |
| os         | File management          |
| subprocess | IP scanning              |
| pillow     | Custom GUI graphics      |

---

## **4. _System Design_**

### **4.1 _Architecture_**

This project follows the **Client–Server Model**.

**Attacker (Client):**  
- Generates simulated attacks  
- Scans network IP addresses  
- Provides attack control interface  

**Mitigator (Server):**  
- Listens on port **9999**  
- Detects incoming attacks  
- Logs and displays attack information  
- Generates downloadable reports  

### **4.2 _Workflow_**

1. Start the **Mitigator server**  
2. Attacker scans the **local network**  
3. User selects **attack type**  
4. Attacker sends **attack signal**  
5. Mitigator logs and displays the **attack**

---

## **5. _Features_**

### **_Attacker Application_**

- GUI-based control panel  
- Supports multiple attack types  
- Network IP scanner  
- Multi-threaded ping scanning  
- Saves previous IP for reuse  
- Clean modern interface  

### **_Mitigator Application_**

- Real-time attack detection  
- Live attack monitoring  
- Automatic log file generation  
- Downloadable reports  
- Scrollable attack history  
- Auto-start server option  

---

## **6. _Testing_**

| Test Case          | Expected Outcome            | Result |
|-------------------|----------------------------|--------|
| Server startup     | Server starts correctly    | ✅ Pass |
| Attack transmission| Attack delivered to Mitigator | ✅ Pass |
| Log generation     | Logs recorded properly     | ✅ Pass |
| GUI update         | Logs displayed in real time | ✅ Pass |
| File saving        | Logs saved to Desktop      | ✅ Pass |
| Multithreading     | Stable concurrent operation | ✅ Pass |

---

## **7. _Sample Attack Log_**

NEW ATTACK DETECTED!
Attack Type: DDoS
Attacker IP: 192.168.1.10
Attacker Port: 53241
Time of Attack: 14:32:11
Day of Attack: Monday, 30 December 2025
Action Taken: Action taken against attacker 192.168.1.10 ...

---

## **8. _Learning Outcomes_**

This project helps in understanding:

- Network attack behavior  
- Client-server communication  
- Socket programming  
- Multithreading concepts  
- GUI development  
- Logging and monitoring systems  
- Cybersecurity defense mechanisms  

---

## **9. _Future Enhancements_**

- Authentication system  
- Encrypted communication  
- Real-time traffic analysis  
- AI-based detection system  
- Web-based monitoring dashboard  

---

## **10. _Conclusion_**

This project demonstrates how network attacks can be simulated and how an effective mitigation system can detect, log, and respond to them.  
It serves as a complete academic cybersecurity project integrating **networking**, **security**, and **software development**.

---

## **_Disclaimer_**

This project is strictly for **academic and educational purposes**.  
It must not be used on real networks without proper authorization.

---

## **_Author_**

**Nayyab Gul**  
*Cybersecurity & Software Engineering Project*

