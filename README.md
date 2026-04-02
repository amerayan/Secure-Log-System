# Secure-Log-System
A secure log system ensures “logs cannot be secretly changed, deleted, or accessed by unauthorized people.”
**Objectives**
Capture system and user activity logs
Prevent unauthorized modification or deletion of logs
Ensure secure storage and transmission of logs
Detect tampering attempts
Provide audit trails for security analysis

**SYSTEM ARCHITECTURE**
*User/System Activity
        ↓
   Log Generator
        ↓
 Secure Log Storage (Encrypted)
        ↓
 Integrity Checker (Hashing)
        ↓
 Monitoring & Alerts**

**PEOJECT STRUCTURE**.
secure-log-system/
│── logs/
│── src/
│   ├── logger.py
│   ├── encrypt.py
│   ├── integrity.py
│   ├── auth.py
│── database/
│── README.md
│── requirements.txt
