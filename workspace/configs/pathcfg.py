import os
import sys
from Utils.debugformat import INFO, DEBUG, WARNING


class cfg:
    def __init__(self):
        self.root = os.getcwd()[:os.getcwd().find("workspace")] + "workspace/"
        self.model = os.path.join(self.root, "models")
        self.utils = os.path.join(self.root, "Utils")
        self.output = os.path.join(self.root, "output")
        self.input = os.path.join(self.root, "input")
        self.configs = os.path.join(self.root, "configs")
        self.LLMPath = "../THUDM/chatglm2-6b"
        self.maxRework = 15
        self.maxReworkOfDetail = 15
        self.csvPath = os.path.join(self.output, "csv")
        self.txtPath = os.path.join(self.output, "text")
        self.jsonPath = os.path.join(self.output, "json")


Pcfg = cfg()
sys.path.append(Pcfg.root)
sys.path.append(Pcfg.model)
sys.path.append(Pcfg.utils)
sys.path.append(Pcfg.output)
sys.path.append(Pcfg.configs)
sys.path.append(Pcfg.LLMPath)
INFO("path loaded successfully")