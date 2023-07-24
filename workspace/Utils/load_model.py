from transformers import AutoTokenizer, AutoModel
from configs.pathcfg import Pcfg
from Utils.debugformat import INFO, DEBUG, WARNING

class chatglm:
    def __init__(self):
        INFO("loading ChatGLM2-6B")
        DEBUG(f"LLMPath:{Pcfg.LLMPath}")
        route = Pcfg.LLMPath
        self.tokenizer = AutoTokenizer.from_pretrained(route, trust_remote_code=True, revision="v1.0")
        self.model_0 = AutoModel.from_pretrained(route, trust_remote_code=True, device='cuda', revision="v1.0")
        self.model = self.model_0.eval()
        INFO("load ChatGLM2-6B successfully")

    def response(self, textIn, history=None):
        try:
            if history==None:
                history = []
            res, history = self.model.chat(self.tokenizer, textIn, history=history)
            return res
        except Exception as e:
            return -1, e
        
if __name__ == "__main__":
    model = chatglm()
    print(model.response("你好呀"))