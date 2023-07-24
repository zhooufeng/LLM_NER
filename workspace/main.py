from configs.pathcfg import Pcfg
from models import promptMain
from Utils.load_model import chatglm
from Utils.debugformat import INFO, DEBUG, WARNING


class Runner:
    def __init__(self):
        self.model = chatglm()

    def Run(self, Text):
        return promptMain.process(Text=Text, model=self.model)

    def checkModel(self):
        checkQuestion = "讲一下机器人三大定律"
        Response = self.model.response(checkQuestion)
        DEBUG(f"Checking ChatGLM model\n\tQuestion: {checkQuestion}\n\tResponse: {Response}")
        if Response[0] == -1:
            WARNING("Fail to check model, error messages are below")
            raise Response[1]
        else:
            INFO("model works fine!!!")

if __name__ == '__main__':
    A = Runner()
    A.checkModel()