# hh8-minor-project-2

Secure File Deletion Tool

A cybersecurity-focused application that ensures **permanent and irreversible deletion**
of sensitive files using **encryption, multi-pass overwriting, and audit logging**.

Problem Statement
Normal file deletion only removes file references.
The actual data remains recoverable using forensic tools.

Solution
This project securely deletes files by:
- Encrypting file contents
- Overwriting data multiple times
- Logging deletion actions for audit proof

Features
- Real secure file deletion
- Multiple overwrite levels (1 / 7 / 35 passes)
- Encryption before deletion
- Audit log generation
- Safe demo mode (no real deletion)

Demo vs Real Deletion
->Normal Delete 
Data recoverable 
No overwrite
No audit log 
->Secure Delete
Data destroyed
Multi-pass overwrite
Logged proof

Screenshots

Main Interface
[Home](screenshots/home.png)

Demo Mode
[Demo](screenshots/demo.png)

Secure Deletion Result
[Result](screenshots/result.png)

Audit Log Proof
[Log](screenshots/log.png)

Cybersecurity Relevance
- Data sanitization
- Anti-forensics
- Secure data disposal
- Compliance & audit logging

Tech Stack
- Python
- Flask
- Cryptography
- File System Operations

Conclusion
This project demonstrates how secure deletion protects data confidentiality
beyond traditional file removal methods.
