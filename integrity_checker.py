"""
File Integrity Checker
====================

A Python-based security tool for monitoring and protecting critical files and directories
by detecting unauthorized modifications, deletions, and additions.

Features:
- SHA-256 hash-based file integrity checking
- JSON configuration and reporting
- Email alerts for detected changes
- Continuous monitoring with configurable intervals
- Cross-platform support (Windows, Linux, macOS)
"""

import hashlib
import os
import json
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class FileIntegrityChecker:
    """Main class for file integrity monitoring and checking"""
    
    def __init__(self, config_file='integrity_config.json'):
        """
        Initialize the File Integrity Checker
        
        Args:
            config_file (str): Path to configuration file (default: 'integrity_config.json')
        """
        self.config_file = config_file
        self.baseline_file = 'baseline_hashes.json'  # File to store baseline hashes
        self.load_config()
        
    def load_config(self):
        """
        Load configuration from JSON file.
        Creates default configuration if file doesn't exist.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            # Default configuration
            self.config = {
                'monitor_paths': [],        # List of files/directories to monitor
                'check_interval': 60,       # Interval between checks (in seconds)
                'alert_email': None,         # Email address for alerts
                'report_dir': 'reports'      # Directory for storing reports
            }
            self.save_config()
            
    def save_config(self):
        """Save current configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
            
    def calculate_hash(self, file_path):
        """
        Calculate SHA256 hash of a file
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            str: SHA256 hash of the file, or None if error occurs
        """
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(byte_block)
            return hash_sha256.hexdigest()
        except Exception as e:
            print(f"Error calculating hash for {file_path}: {str(e)}")
            return None
            
    def create_baseline(self):
        """
        Create baseline hash for all monitored files
        Stores hashes in baseline_hashes.json
        """
        baseline = {}
        for path in self.config['monitor_paths']:
            if os.path.isfile(path):
                baseline[path] = self.calculate_hash(path)
            elif os.path.isdir(path):
                # Recursively process directory
                for root, _, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        baseline[file_path] = self.calculate_hash(file_path)
        
        with open(self.baseline_file, 'w') as f:
            json.dump(baseline, f, indent=4)
        print("Baseline hashes created successfully.")
        
    def check_integrity(self):
        """
        Check file integrity against baseline
        
        Returns:
            None: Generates report and sends alert if changes detected
        """
        if not os.path.exists(self.baseline_file):
            print("No baseline found. Please create a baseline first.")
            return
            
        with open(self.baseline_file) as f:
            baseline = json.load(f)
            
        # Initialize report structure
        report = {
            'timestamp': datetime.now().isoformat(),
            'changes': [],          # List of modified files
            'missing_files': [],    # List of missing files
            'new_files': []        # List of new files
        }
        
        # Check existing files
        for file_path, expected_hash in baseline.items():
            if not os.path.exists(file_path):
                report['missing_files'].append(file_path)
                continue
                
            current_hash = self.calculate_hash(file_path)
            if current_hash != expected_hash:
                report['changes'].append({
                    'file': file_path,
                    'expected_hash': expected_hash,
                    'current_hash': current_hash
                })
                
        # Check for new files
        for path in self.config['monitor_paths']:
            if os.path.isfile(path) and path not in baseline:
                report['new_files'].append(path)
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if file_path not in baseline:
                            report['new_files'].append(file_path)
                            
        self.generate_report(report)
        if report['changes'] or report['missing_files']:
            self.send_alert(report)
            
    def generate_report(self, report):
        """
        Generate integrity report in JSON format
        
        Args:
            report (dict): Report data to be saved
        """
        if not os.path.exists(self.config['report_dir']):
            os.makedirs(self.config['report_dir'])
            
        # Create timestamped report file
        report_file = os.path.join(self.config['report_dir'], 
                                 f"integrity_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=4)
        print(f"Integrity report generated: {report_file}")
        
    def send_alert(self, report):
        """
        Send email alert if configured
        
        Args:
            report (dict): Report data to be sent
        """
        if not self.config['alert_email']:
            return
            
        try:
            # Create email message
            msg = MIMEText(json.dumps(report, indent=4))
            msg['Subject'] = 'File Integrity Alert'
            msg['From'] = 'integrity_checker@system'
            msg['To'] = self.config['alert_email']
            
            # Send email via local SMTP server
            with smtplib.SMTP('localhost') as server:
                server.send_message(msg)
            print("Alert email sent successfully.")
        except Exception as e:
            print(f"Failed to send alert email: {str(e)}")
            
    def monitor(self):
        """
        Continuous monitoring of files
        Runs integrity checks at configured intervals
        """
        print("Starting file integrity monitoring...")
        try:
            while True:
                self.check_integrity()
                time.sleep(self.config['check_interval'])
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")

if __name__ == "__main__":
    # Example usage
    checker = FileIntegrityChecker()
    
    # Configure monitoring paths and email
    checker.config['monitor_paths'] = ['/path/to/monitor']
    checker.config['alert_email'] = 'admin@example.com'
    checker.save_config()
    
    # Create baseline and start monitoring
    checker.create_baseline()
    checker.monitor()
