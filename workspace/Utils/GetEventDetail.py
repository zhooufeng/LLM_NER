import random
try:
    from load_model import chatglm
    from extractJson import extractJson
except:
    pass
background = """
我希望你能够以一名语言学家的身份完成我的任务。

首先我会给你一段文字，然后我会给你一个该段文字中发生过的事件的事件类型。

你需要做的事情是，根据该事件的事件类型，提取出文字中事件的细节，严格以json格式输出。
"""
Example1 = """
例子：

文字：研究人员近期捕获了一起针对巴基斯坦木尔坦地区武装力量的网络攻击事件，攻击者以木尔坦的罗德兰区基于情报的反恐行动(intelligence-based operation，IBO)报告为诱饵，尝试投递一种变种木马程序MessPrint以控制受害者设备。

事件类型：攻击事件

输出：{}
""".format({"攻击对象": "巴基斯坦木尔坦地区武装力量", "攻击者": "未知", "攻击手段": "投递一种变种木马程序", "攻击工具": "MessPrint"})
Example2 = """
例子：

文字：Gelsemium是一个自2014年以来活跃的网络间谍组织，主要针对的目标包括东亚和中东的政府、大学、电子制造商和宗教组织。攻击手法为使用带有文档附件的鱼叉式网络钓鱼电子邮件，利用CVE-2012-0158 Microsoft Office漏洞来传播恶意软件。

事件类型：间谍活动

输出：{}
""".format({"间谍身份": "Gelsemium", "间谍工作目标": "政府、大学、电子制造商和宗教组织", "活跃时间": "2014年以来"})
Example3 = """
例子：

文字：近期，研究人员发现了一批疑似APT-C-56（透明部落）针对恐怖主义发起攻击的恶意样本，通过溯源关联分析发现，攻击活动至少开始于2018年6月，至今仍处于活跃状态。

事件类型：发现样本

输出：{}
""".format({"样本情况": "疑似APT-C-56（透明部落）针对恐怖主义发起攻击", "发现方法": "溯源关联分析", "发现人": "研究人员"})
Question1 = """
问题：

文字：{}

事件类型：{}

输出：
"""


def GetEventDetail(text, EventType, model=None):
    prompt = background + Example1 + Example2 + Example3 + Question1.format(text, EventType)
    if model is None:
        model = chatglm()
    return model.response(prompt)[0].replace("\'", "\"")


if __name__ == "__main__":
    text = "近日，研究人员发现SteamHide恶意软件滥用Steam游戏平台进行传播。攻击者通过在Steam平台上更新个人资料头像将恶意软件以加密的形式隐藏其中。Steam平台只是承载恶意文件的工具。下载、解包和执行恶意负载的繁重工作由一个外部组件处理，该组件访问一个Steam配置文件上的图像。"
    EventType = "漏洞事件"
    # print(GetEventDetail(text, EventType))
    print(Example2)
    print(Question1.format(text, EventType))