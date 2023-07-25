import json

from configs.pathcfg import Pcfg
import pprint
import tqdm
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

    def RunInBatches(self, TextList, savePath=None):
        INFO(f"启用多文本分析模式，共{len(TextList)}文本")
        res = []
        cnt = 1
        for i in TextList:
            INFO(f"分析文本({cnt}/{len(TextList)})\n")
            res.append(promptMain.process(Text=i, model=self.model))
            cnt += 1
            if savePath==None:
                with open(Pcfg.jsonPath + "/debug.json", "w", encoding='utf-8') as f:
                    json.dump(res, f)
            else:
                with open(savePath, "w", encoding='utf-8') as f:
                    json.dump(res, f)
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
    近日，研究人员发现SteamHide恶意软件滥用Steam游戏平台进行传播。攻击者通过在Steam平台上更新个人资料头像将恶意软件以加密的形式隐藏其中。Steam平台只是承载恶意文件的工具。下载、解包和执行恶意负载的繁重工作由一个外部组件处理，该组件访问一个Steam配置文件上的图像。
    """
    TextList = [
        debugText, debugText
    ]
    # print(A.Run(debugText))
    res = A.RunInBatches(TextList, savePath=Pcfg.jsonPath + "/debug1.json")
    # res = A.Run(debugText)
    # pprint.pprint(res)
