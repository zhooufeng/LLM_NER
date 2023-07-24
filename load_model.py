from transformers import AutoTokenizer, AutoModel


class chatglm:
    def __init__(self):
        route = "THUDM/chatglm2-6b"
        self.tokenizer = AutoTokenizer.from_pretrained(route, trust_remote_code=True, revision="v1.0")
        self.model_0 = AutoModel.from_pretrained(route, trust_remote_code=True, device='cuda', revision="v1.0")
        self.model = self.model_0.eval()

    def response(self, textIn, history=None):
        if history==None:
            history = []
        res, history = self.model.chat(self.tokenizer, textIn, history=history)
        return res, history
        
if __name__ == "__main__":
    model = chatglm()
    print(model.response("你好呀"))