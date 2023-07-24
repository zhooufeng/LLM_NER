from configs.pathcfg import Pcfg
from models import promptMain
from Utils.load_model import chatglm
from Utils.debugformat import INFO, DEBUG, WARNING


class Runner:
    def __init__(self):
        self.model = chatglm()

    def Run(self, Text):
        backCar = '\n'
        INFO(f"启用单文本分析模式，文本长度:{len(Text)}，文本摘要:{Text.replace(backCar, '')[:10]}")
        return promptMain.process(Text=Text, model=self.model)

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
    **标题：医学科技突破！智能纳米机器人成功治愈癌症病例**

**日期：2023年7月24日**

**全球范围内，医学科技再次取得巨大突破，一项引人瞩目的研究成果在今日揭晓。科学家们成功研发出智能纳米机器人，这一技术在临床试验中首次应用于癌症治疗，成功治愈了数位癌症患者。**

**这些微小但卓越的纳米机器人由国际一流的跨学科团队合作开发，融合了纳米科学、生物医学和人工智能领域的最新进展。它们被设计成能够精确地定位和攻击癌细胞，并在体内进行精准的药物释放，同时最大程度上减少对健康细胞的损伤。**

**一位参与研究的医学科学家，杰出的癌症学专家Dr. Emily Chen博士表示：“这是医学史上的重大突破之一。我们通过纳米技术的应用，将治疗精确度推向了一个前所未有的高度。智能纳米机器人不仅能够定位癌细胞，还能即时适应细胞的变化，并根据患者的个体特征进行定制化治疗。”**

**在最初的临床试验中，智能纳米机器人被应用于晚期乳腺癌和肺癌患者的治疗。令人鼓舞的是，乳腺癌患者中有超过80%的病例获得了完全缓解，而肺癌患者的治疗成功率也达到了惊人的60%。研究团队计划在未来数年内扩大试验范围，将其应用于更多癌症类型的治疗，以进一步验证其疗效和安全性。**

**除了治疗方面的巨大突破，智能纳米机器人在癌症筛查、早期诊断和个体化治疗上也有着广阔的应用前景。该技术有望彻底改变癌症治疗的格局，使得越来越多的患者能够获得更为有效和精准的医疗帮助。**

**然而，科学家们也强调，虽然取得了显著的进展，但智能纳米机器人在大规模应用前仍需进行更多长期的安全性和效果评估。世界各国政府和医疗机构将继续密切关注这一前沿技术的发展，以确保其在未来能够为更多患者带来福音。**

**整个医学界对这一突破性的研究成果充满期待，相信未来的医学科技将继续探索和创新，为人类健康带来更多奇迹。**
    """
    A.Run(debugText)