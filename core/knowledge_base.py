"""
knowledge_base.py
Author: Tasya
Date: 12-10-2025

Class untuk mengelola Knowledge Base (IF-THEN rules) sistem pakar.
"""

from utils.rule_loader import load_rules

class KnowledgeBase:
    """
    Class KnowledgeBase untuk menyimpan dan memanipulasi rules.
    """

    def __init__(self, rules_file):
        self.rules_file = rules_file
        self.rules = self.load_rules()

    def load_rules(self):
        """Load rules dari file JSON."""
        return load_rules(self.rules_file)

    def add_rule(self, rule_id, antecedent, consequent, cf=1.0):
        """Tambah rule baru ke Knowledge Base."""
        self.rules[rule_id] = {"IF": antecedent, "THEN": consequent, "CF": cf}

    def get_rules(self):
        """Mengembalikan semua rules."""
        return self.rules
