# interface.py
from core.knowledge_base import KnowledgeBase
from core.working_memory import WorkingMemory
from core.inference_engine import InferenceEngine

class ExpertSystemInterface:
    """Interface penghubung antara GUI dan engine."""

    def __init__(self, rules_path="data/rules.json"):
        self.kb = KnowledgeBase(rules_path)
        self.memory = WorkingMemory()
        self.engine = InferenceEngine(self.kb, self.memory)

    def diagnosa(self, gejala_terpilih):
        """Menambahkan gejala ke memory dan jalankan forward chaining."""
        self.memory.clear()
        for g in gejala_terpilih:
            self.memory.add_fact(g)
        return self.engine.forward_chain()
