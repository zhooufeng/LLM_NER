from load_model import chatglm
from EventList import EventList

background = """
我希望你能够以一名语言学家的身份完成我的任务。

首先我会给你一段文字，然后我会给你备选的事件类型列表。

你需要做的事情是，从备选的事件类型列表中选出一个最符合文字中描述情境的事件类型然后输出。
"""
Example1 = """
例子1：

文字：研究人员近期捕获了一起针对巴基斯坦木尔坦地区武装力量的网络攻击事件，攻击者以木尔坦的罗德兰区基于情报的反恐行动(intelligence-based operation，IBO)报告为诱饵，尝试投递一种变种木马程序MessPrint以控制受害者设备。

备选事件类型列表：{}

输出：攻击事件
""".format(EventList)
Example2 = """
例子2：

文字：Gelsemium是一个自2014年以来活跃的网络间谍组织，主要针对的目标包括东亚和中东的政府、大学、电子制造商和宗教组织。攻击手法为使用带有文档附件的鱼叉式网络钓鱼电子邮件，利用CVE-2012-0158 Microsoft Office漏洞来传播恶意软件。

备选事件类型列表：{}

输出：恶意软件事件
""".format(EventList)
Example3 = """
例子2：

文字：样本伪装成xls的scr文件,会释放持久化组件与RAT对中招用户持续监控。

备选事件类型列表：{}

输出：监控
""".format(EventList)
Question1 = """
问题1：

文字：{}

备选事件类型列表：{}

输出：
"""

def GetEventType(text, model=None):
    prompt = background + Example1 + Example2 + Example3 + Question1.format(text, EventList)
    if model == None:
        model = chatglm()
    return model.response(prompt)[0]


if __name__ == "__main__":
    text = "近日，研究人员发现SteamHide恶意软件滥用Steam游戏平台进行传播。攻击者通过在Steam平台上更新个人资料头像将恶意软件以加密的形式隐藏其中。Steam平台只是承载恶意文件的工具。下载、解包和执行恶意负载的繁重工作由一个外部组件处理，该组件访问一个Steam配置文件上的图像。"
    print(GetEventType(text))