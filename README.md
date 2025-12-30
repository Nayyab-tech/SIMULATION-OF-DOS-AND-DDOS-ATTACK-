# 🛡️ DoS & DDoS Attack Simulation with Mitigation System

A complete cybersecurity academic project demonstrating network attacks and their real-time mitigation using Python.

---

## 📌 **Introduction**

The **DoS & DDoS Attack Simulation with Mitigation System** is a Python-based cybersecurity project that demonstrates how different types of network attacks can be simulated and how a defensive system can detect, log, and respond to these attacks in real time.

This project provides hands-on understanding of:

- 🧠 Networking principles
- 🧵 Multithreading
- 🔌 Socket programming
- 🛡️ Security monitoring systems

---

## 🎯 **Objectives**

- 🔥 Simulate cyber attacks: DoS, DDoS, SYN Flood, SQL Injection, UDP Flood
- 🛡️ Build a real-time mitigation engine
- 🔄 Understand client-server communication
- 🖥️ Design user-friendly GUIs using Tkinter
- ⚙️ Apply multithreading for concurrent execution

---

## 🖥️ **System Requirements**

### 💻 **Hardware Requirements**

| Component    | Requirement          |
|--------------|----------------------|
| Processor    | 1 GHz or faster      |
| RAM          | 2 GB minimum         |
| Hard Disk    | 500 MB free space    |

### 🧰 **Software Requirements**

- Python 3.9+
- Windows OS (Recommended)

### 📦 **Required Libraries**
pip install pillow

### 📚 **Standard Libraries Used**

`socket, threading, datetime, tkinter, os, subprocess, platform`

### 🧩 **Library Roles**

| Library     | Purpose              |
|-------------|----------------------|
| socket      | Network communication|
| threading   | Parallel execution   |
| tkinter     | GUI development      |
| datetime    | Time logging         |
| os          | File management      |
| subprocess  | IP scanning          |
| pillow      | GUI graphics         |

---

## 🏗️ **System Design**

### 🧱 **Architecture**

**Client-Server Model**

- **🧨 Attacker (Client)**
  - Generates attack traffic
  - Scans network IPs
  - GUI-based attack controller

- **🛡️ Mitigator (Server)**
  - Listens on Port 9999
  - Detects malicious activity
  - Logs & displays attacks
  - Generates downloadable reports

### 🧭 **Workflow**

`Start Server → Scan Network → Select Attack → Launch Attack → Detect → Log → Report`

---

## ✨ **Features**

### 🧨 **Attacker Application**

- 🎛️ GUI control panel
- ⚔️ Multiple attack simulations
- 🌐 Network IP scanner
- 🧵 Multi-threaded ping scanning
- 💾 IP history saving
- 🎨 Clean modern interface

### 🛡️ **Mitigator Application**

- 🚨 Live attack detection
- 📊 Real-time monitoring
- 🗂️ Auto log generation
- 📥 Downloadable reports
- 📜 Scrollable attack history

---

## 🧪 **Testing Results**

| Test Case              | Status |
|------------------------|--------|
| Server startup         | ✅ Pass |
| Attack delivery        | ✅ Pass |
| Log generation         | ✅ Pass |
| Live GUI updates       | ✅ Pass |
| File saving            | ✅ Pass |
| Multithreading stability | ✅ Pass |

---

## 📜 **Sample Attack Log**

NEW ATTACK DETECTED!

Attack Type: DDoS
Attacker IP: 192.168.1.10
Attacker Port: 53241
Time: 14:32:11
Day: Monday, 30 December 2025
Action: Attacker blocked and logged.


---

## 🎓 **Learning Outcomes**

- ✔ Network attack behavior
- ✔ Client-server architecture
- ✔ Python socket programming
- ✔ Multithreading concepts
- ✔ GUI development
- ✔ Security logging systems
- ✔ Cyber defense mechanisms

---

## 🚀 **Future Enhancements**

- 🔐 Authentication system
- 🔒 Encrypted communication
- 📈 Real-time traffic analysis
- 🤖 AI-based detection
- 🌐 Web-based monitoring dashboard

---

## 🧾 **Conclusion**

This project successfully demonstrates how cyber attacks can be simulated and how an effective mitigation system can detect, log, and neutralize malicious activity in real time — making it a strong academic cybersecurity solution.

---

## ⚠️ **Disclaimer**

**This project is strictly for educational purposes only.**  
**Do NOT deploy on real networks without proper authorization.**

---

## 👨‍💻 **Author**

**Nayyab Gul and Laiba Naeem**  
*Cybersecurity & Software Engineering Project*



