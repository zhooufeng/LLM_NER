from configs.pathcfg import Pcfg
from models import promptMain
from Utils.load_model import chatglm
from Utils.debugformat import INFO, DEBUG, WARNING


class Runner:
    def __init__(self):
        self.model = chatglm()

    def Run(self, Text):
        backCar = '\n'
        space = ' '
        INFO(f"启用单文本分析模式，文本长度:{len(Text)}，文本摘要:{Text.replace(backCar, '').replace(space, '')[:10]}")
        return promptMain.process(Text=Text, model=self.model)

    def RunInBatches(self, TextList):
        INFO(f"启用多文本分析模式，共{len(TextList)}文本")
        res = []
        for i in TextList:
            res.append(promptMain.process(Text=i, model=self.model))
        return res

    def checkModel(self):
        checkQuestion = "讲一下机器人三大定律"
        Response = self.model.response(checkQuestion)
        DEBUG(f"Checking ChatGLM model\n\tQuestion: {checkQuestion}\n\tResponse: {Response[0]}")
        if Response[0] == -1:
            WARNING("Fail to check model, error messages are below")
            raise Response[1]
        else:
            INFO("model works fine!!!")

if __name__ == '__main__':
    A = Runner()
    # A.checkModel()
    debugText = """
    会议指出，当前经济运行面临新的困难挑战，主要是国内需求不足，一些企业经营困难，重点领域风险隐患较多，外部环境复杂严峻。疫情防控平稳转段后，经济恢复是一个波浪式发展、曲折式前进的过程。我国经济具有巨大的发展韧性和潜力，长期向好的基本面没有改变。
    """
    print(A.Run(debugText))
