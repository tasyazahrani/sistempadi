"""
rule_loader.py
Author: Tasya
Date: 12-10-2025

Fungsi utility untuk load/save rules JSON.
"""

import json

def load_rules(file_path):
    """
    Load rules dari file JSON.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def save_rules(file_path, rules):
    """
    Simpan rules ke file JSON.
    """
    with open(file_path, 'w') as f:
        json.dump(rules, f, indent=4)
