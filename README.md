# 🛡️ AI SOC Analyst Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-Free-4285F4?style=for-the-badge&logo=google&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE_ATT%26CK-Mapped-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered Security Operations Centre assistant that analyzes security logs in seconds, maps findings to MITRE ATT&CK, and generates professional PDF reports.**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [Screenshots](#screenshots) • [Tech Stack](#tech-stack)

</div>

---

## 🎯 What Is This?

Most SOC analysts spend hours manually reading through thousands of security logs trying to identify threats. This tool changes that.

Paste any security log — from Wazuh, Windows Event Logs, Apache, Syslog — and the AI instantly tells you:

- ✅ Was an attack detected?
- ✅ What type of attack is it?
- ✅ What MITRE ATT&CK technique was used?
- ✅ What severity level is this?
- ✅ What immediate actions should you take?
- ✅ Full investigation steps

All in under 5 seconds. All exportable as a professional PDF report.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 AI Log Analysis | Paste any security log and get instant AI-powered analysis |
| 🎯 MITRE ATT&CK Mapping | Every finding mapped to real ATT&CK technique IDs |
| 📊 Severity Classification | Critical / High / Medium / Low / Info ratings |
| 📄 PDF Report Export | Professional client-ready reports in one click |
| 📈 Analysis History | SQLite database tracking all past analyses |
| 🧪 Sample Logs | Built-in samples for brute force, SQLi, malware, privilege escalation |
| 📡 Live Statistics | Real-time dashboard stats — total analyses, critical alerts, attacks |
| 🔍 Investigation Steps | AI-generated step-by-step response guide |
| ⚡ False Positive Rating | AI confidence score and false positive likelihood |
| 🌐 Web Interface | Clean dark-themed SOC dashboard UI |

---

## 🖥️ Demo

### Detecting a Brute Force Attack
```
Input Log:
Mar 29 17:54:33 server sshd[1234]: Failed password for admin from 192.168.1.100
Mar 29 17:54:34 server sshd[1235]: Failed password for root from 192.168.1.100
Mar 29 17:54:35 server sshd[1236]: Failed password for admin from 192.168.1.100

AI Output:
✅ Attack Detected: YES
🔴 Severity: HIGH
🎯 Attack Type: SSH Brute Force Attack
📌 MITRE Technique: T1110 - Brute Force
📌 MITRE Tactic: Credential Access
🔍 Summary: Multiple failed SSH login attempts detected from single IP...
⚡ Immediate Actions: Block IP 192.168.1.100, Enable account lockout policy...
🔎 Investigation Steps: Check auth.log for successful logins, Verify...
```

### Logs Supported
- 🐧 Linux Syslog / Auth.log
- 🪟 Windows Event Logs
- 🛡️ Wazuh SIEM Alerts
- 🌐 Apache / Nginx Access Logs
- 🔥 Firewall Logs
- 🔑 SSH Authentication Logs
- 📱 Any custom log format

---

## ⚡ Quick Start

### Prerequisites
```bash
Python 3.10+
pip
A free Gemini API key (aistudio.google.com)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-soc-assistant.git
cd ai-soc-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your Gemini API key
```

### Get Your Free API Key

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with Google account
3. Click **Get API Key**
4. Copy and paste into your `.env` file

**No credit card required. Completely free.**

### Run The App

```bash
python app.py
```

Open your browser and go to `http://localhost:5000`

---

## 📁 Project Structure

```
ai-soc-assistant/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── .env.example            # Environment template
├── soc.db                  # SQLite database (auto-created)
│
├── templates/
│   └── index.html          # Main dashboard UI
│
├── static/
│   └── (CSS/JS assets)
│
├── reports/
│   └── (Generated PDF reports saved here)
│
└── README.md
```

---

## 🚀 Usage

### Basic Log Analysis
1. Open `http://localhost:5000`
2. Paste your security log in the input box
3. Click **Analyze with AI**
4. View results in the right panel

### Using Sample Logs
Click any sample button to load pre-built test cases:
- **Brute Force** — SSH password attack simulation
- **SQL Injection** — Web application attack logs
- **Malware** — Suspicious process execution
- **Priv Escalation** — Windows privilege escalation
- **Normal Log** — Baseline for false positive testing

### Exporting PDF Reports
1. Run an analysis
2. Click **Export PDF Report**
3. Professional report downloads automatically
4. Ready to share with clients or managers

---

## 🔍 Sample Outputs

### Brute Force Detection
```json
{
  "attack_detected": true,
  "attack_type": "SSH Brute Force Attack",
  "severity": "High",
  "mitre_technique": "T1110 - Brute Force",
  "mitre_tactic": "Credential Access",
  "confidence": "94%",
  "false_positive_chance": "Low",
  "immediate_actions": [
    "Block source IP 192.168.1.100 at firewall",
    "Enable account lockout after 5 failed attempts",
    "Check for any successful logins from this IP"
  ]
}
```

### Privilege Escalation Detection
```json
{
  "attack_detected": true,
  "attack_type": "Privilege Escalation - Admin Group Modification",
  "severity": "Critical",
  "mitre_technique": "T1484 - Domain Policy Modification",
  "mitre_tactic": "Defense Evasion, Privilege Escalation",
  "confidence": "97%",
  "false_positive_chance": "Low"
}
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core backend language |
| Flask | Web framework |
| Google Gemini API | AI analysis engine (free) |
| SQLite | Analysis history database |
| FPDF2 | PDF report generation |
| HTML/CSS/JS | Frontend dashboard |
| python-dotenv | Environment management |

---

## 📦 Requirements

```
flask>=2.3.0
google-generativeai>=0.3.0
fpdf2>=2.7.0
python-dotenv>=1.0.0
```

---

## 🔐 Security & Ethics

> ⚠️ **DISCLAIMER**: This tool is built for educational purposes and authorized security monitoring only. Do not use to analyze logs from systems you do not own or have explicit permission to monitor.

- API keys are stored in `.env` file (never committed to Git)
- `.gitignore` excludes all sensitive files
- No log data is sent to external servers except the AI API
- All analysis history stored locally in SQLite

---

## 🗺️ Roadmap

- [ ] Add OpenAI / Claude API support as alternatives
- [ ] Real-time Wazuh log ingestion via webhook
- [ ] Email alerting for Critical severity findings
- [ ] Multi-log batch analysis
- [ ] STIX/TAXII threat intelligence integration
- [ ] Dockerize for easy deployment
- [ ] REST API endpoints for integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Share your use cases

---

## 👤 Author

**Alan Shinto**
- 🎓 CEH v13 | ADCD — Redteam Hacker Academy, Calicut
- 🔗 LinkedIn: [linkedin.com/in/alan-shinto](https://linkedin.com/in/alan-shinto)
- 🐙 GitHub: [github.com/killu-alansh](https://github.com/killu-alansh)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

It helps other cybersecurity students discover this tool.

---

<div align="center">
Built with ❤️ for the cybersecurity community
</div>
