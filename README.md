# FILE INTEGRITY CHECKER

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: NARENDRA VIJAY BORHADE

*INTERN ID*: CT4MNLF

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 16 weeks

*MENTOR*: NEELA SANTOSH

*DESCRIPTION OF TASK*: The File Integrity Checker is a comprehensive Python-based security tool designed to monitor and protect critical files and directories by detecting unauthorized modifications, deletions, and additions. This system provides a robust solution for maintaining file system integrity through continuous monitoring, detailed reporting, and alerting mechanisms.

Platform and Technical Specifications:

Programming Language: Python 3.x
Operating System: Cross-platform (Windows, Linux, macOS)
Dependencies: Standard Python libraries (hashlib, os, json, time, smtplib, email)
Configuration Format: JSON
Hash Algorithm: SHA-256
Reporting Format: JSON
Email Protocol: SMTP
File System Support: Works with all major file systems (NTFS, ext4, APFS, etc.)
The system operates by creating cryptographic hashes (SHA-256) of monitored files and comparing them against a baseline. This approach ensures that even the smallest changes to file content are detected. The system is highly configurable through a JSON configuration file (integrity_config.json), which allows users to specify monitoring paths, check intervals, and email alert settings.

The system's architecture consists of several key components. The configuration management module handles the loading and saving of settings, automatically creating a default configuration if none exists. The integrity checking module is responsible for calculating file hashes, comparing them against the baseline, and identifying changes. The reporting module generates detailed JSON reports that include information about modified files, missing files, and new files. The alerting module sends email notifications when changes are detected, using the local SMTP server.

One of the system's strengths is its flexibility in monitoring. It can monitor individual files or entire directory trees, making it suitable for various use cases. The baseline creation process captures the initial state of monitored files, storing their hashes in baseline_hashes.json. During integrity checks, the system compares current file hashes against this baseline, identifying any discrepancies.

The reporting mechanism is particularly robust, generating timestamped JSON reports in a dedicated 'reports' directory. These reports include detailed information about each detected change, including file paths, expected hashes, and current hashes. This level of detail is invaluable for forensic analysis and incident response.

For organizations requiring immediate notification of integrity violations, the system includes an email alerting feature. When changes are detected, the system sends an email containing the complete report to the configured recipient. This feature uses the local SMTP server, making it easy to integrate with existing email infrastructure.

The continuous monitoring mode allows the system to run indefinitely, checking file integrity at regular intervals. This mode can be stopped gracefully using Ctrl+C, making it suitable for long-term deployment. The check interval is configurable, allowing administrators to balance system load with monitoring frequency.

Security professionals will find this tool particularly valuable for several use cases. It can be used to monitor critical system files, ensuring that unauthorized modifications are detected promptly. Software developers can use it to verify the integrity of their codebase, detecting any unauthorized changes. Organizations can deploy it as part of their security auditing process, maintaining a record of all file system changes.

The technical implementation leverages Python's standard libraries, making the system portable and easy to deploy. The use of SHA-256 for hashing ensures strong cryptographic protection against tampering. The JSON-based configuration and reporting make the system easy to integrate with other tools and processes.

In terms of security applications, the File Integrity Checker is particularly effective in detecting malware infections, as many types of malware modify system files. It can also help identify insider threats by detecting unauthorized access to sensitive files. For compliance purposes, the system provides an auditable record of file system changes, which can be valuable for meeting regulatory requirements.

The system's modular design makes it easy to extend. Additional features could include integration with SIEM systems, support for additional hash algorithms, or the ability to monitor file permissions and ownership changes. The current implementation provides a solid foundation for building more advanced file integrity monitoring solutions.

In conclusion, the File Integrity Checker is a powerful tool for maintaining file system security. Its combination of cryptographic hashing, detailed reporting, and alerting capabilities make it an essential component of any comprehensive security strategy. Whether used for monitoring critical system files, auditing software integrity, or detecting unauthorized changes, this tool provides valuable insights into file system activity and helps organizations maintain the integrity of their digital assets.

Applications:

System Administration:

Monitoring critical system files (e.g., /etc, /bin, /usr)
Detecting unauthorized changes to configuration files
Tracking changes to system binaries
Software Development:

Verifying codebase integrity
Detecting unauthorized modifications to source code
Monitoring build artifacts
Security Operations:

Detecting malware infections
Identifying insider threats
Monitoring sensitive data files
Compliance and Auditing:

Maintaining audit trails of file changes
Meeting regulatory requirements (e.g., PCI DSS, HIPAA)
Providing evidence for forensic investigations
Data Integrity:

Monitoring critical databases
Verifying backup integrity
Detecting unauthorized data modifications
The File Integrity Checker is a versatile tool that can be adapted to various security and monitoring scenarios, making it an essential component of any organization's security infrastructure

#OUTPUT:
[integrity_report_20250215_175521.json](https://github.com/user-attachments/files/18826586/integrity_report_20250215_175521.json)
[integrity_report_20250215_175621.json](https://github.com/user-attachments/files/18826587/integrity_report_20250215_175621.json)
[integrity_report_20250215_175721.json](https://github.com/user-attachments/files/18826596/integrity_report_20250215_175721.json)
[integrity_report_20250215_175734.json](https://github.com/user-attachments/files/18826585/integrity_report_20250215_175734.json)
[integrity_report_20250215_175821.json](https://github.com/user-attachments/files/18826588/integrity_report_20250215_175821.json)
[integrity_report_20250215_175921.json](https://github.com/user-attachments/files/18826590/integrity_report_20250215_175921.json)
[integrity_report_20250215_180021.json](https://github.com/user-attachments/files/18826584/integrity_report_20250215_180021.json)
[integrity_report_20250215_180121.json](https://github.com/user-attachments/files/18826595/integrity_report_20250215_180121.json)
[integrity_report_20250215_175121.json](https://github.com/user-attachments/files/18826593/integrity_report_20250215_175121.json)
[integrity_report_20250215_175221.json](https://github.com/user-attachments/files/18826594/integrity_report_20250215_175221.json)
[integrity_report_20250215_175234.json](https://github.com/user-attachments/files/18826591/integrity_report_20250215_175234.json)
[integrity_report_20250215_175321.json](https://github.com/user-attachments/files/18826589/integrity_report_20250215_175321.json)
[integrity_report_20250215_175421.json](https://github.com/user-attachments/files/18826592/integrity_report_20250215_175421.json)

[file_monitor_logs.txt](https://github.com/user-attachments/files/18826607/file_monitor_logs.txt)
[important_file.txt](https://github.com/user-attachments/files/18826608/important_file.txt)
