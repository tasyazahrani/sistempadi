# main.py
from core.knowledge_base import KnowledgeBase
from core.working_memory import WorkingMemory
from core.inference_engine import InferenceEngine
from ui.gui_interface import GUI  # GUI versi terbaru dengan download history

def main():
    kb = KnowledgeBase("data/rules.json")
    memory = WorkingMemory()
    engine = InferenceEngine(kb, memory)
    
    gui = GUI(engine)
    gui.run()

if __name__ == "__main__":
    main()
