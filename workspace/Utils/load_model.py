from transformers import AutoTokenizer, AutoModel

class chatglm:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("../../chatglm2-6b", trust_remote_code=True)
        self.model_0 = AutoModel.from_pretrained("../../chatglm2-6b", trust_remote_code=True, device='cuda')
        self.model = self.model_0.eval()

    def response(self, textIn, history=None):
        if history==None:
            history = []
        res, history = self.model.chat(self.tokenizer, textIn, history=history)
        return res, history
        
if __name__ == "__main__":
    model = chatglm()
    print(model.response("你好呀"))