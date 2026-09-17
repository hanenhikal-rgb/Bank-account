Bank Account Management System
A lightweight, object-oriented banking application written in Python. It provides core account management capabilities including deposits, withdrawals, balance encapsulation, and global account tracking.

Features
Account Creation: Register accounts with a holder's name, email address, and initial deposit.

Transaction Handling:

Deposit: Add funds with built-in positive-value verification.

Withdrawal: Deduct funds with balance checks to prevent overdrafts.

Encapsulation: Protected balance attribute accessed and mutated safely via @property and @balance.setter decorators.

Account Tracking: Global tracking of the total number of registered accounts via a class variable (account_count).

Prerequisites
Python 3.6+ installed on your system.

No external libraries or packages required.

Installation & Running
Run the application:
python main.py
