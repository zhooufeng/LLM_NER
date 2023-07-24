import os
import sys
from Utils.debugformat import INFO, DEBUG, WARNING


class cfg:
    def __init__(self):
        self.root = os.getcwd()[:os.getcwd().find("workspace")] + "workspace/"
        self.model = os.path.join(self.root, "models")
        self.utils = os.path.join(self.root, "Utils")
        self.output = os.path.join(self.root, "output")
        self.configs = os.path.join(self.root, "configs")
        self.LLMPath = "../THUDM/chatglm2-6b"


Pcfg = cfg()
sys.path.append(Pcfg.root)
sys.path.append(Pcfg.model)
sys.path.append(Pcfg.utils)
sys.path.append(Pcfg.output)
sys.path.append(Pcfg.configs)
sys.path.append(Pcfg.LLMPath)
INFO("path loaded successfully")