from load_model import chatglm
from EventList import EventList

background = """
我希望你能够以一名语言学家的身份完成我的任务。

首先我会给你一段文字，然后我会给你一个你需要重点关注事件的列表。
你需要做的事情是，提取出文字中存在的重点关注事件，以列表形式输出。
"""
Example1 = """
例子1：

文字：研究人员近期捕获了一起针对巴基斯坦木尔坦地区武装力量的网络攻击事件，攻击者以木尔坦的罗德兰区基于情报的反恐行动(intelligence-based operation，IBO)报告为诱饵，尝试投递一种变种木马程序MessPrint以控制受害者设备。

重点关注事件的列表：{}

输出：['恶意软件攻击', '网络攻击']
""".format(EventList)
Example2 = """
例子2：

文字：Gelsemium是一个自2014年以来活跃的网络间谍组织，主要针对的目标包括东亚和中东的政府、大学、电子制造商和宗教组织。攻击手法为使用带有文档附件的鱼叉式网络钓鱼电子邮件，利用CVE-2012-0158 Microsoft Office漏洞来传播恶意软件。

重点关注事件的列表：{}

输出：['间谍攻击活动', '漏洞事件']
""".format(EventList)
Example3 = """
例子3：

文字：IceXLoader是一种商业恶意软件，在黑客论坛中以118美元的价格出售，主要用于在受害主机中下载和执行其他的恶意软件。

重点关注事件的列表：{}

输出：['下载', '间谍攻击活动', '恶意软件攻击']
""".format(EventList)
Question1 = """
问题1：

文字：{}

重点关注事件的列表：{}

输出：
"""

def IdentifyEvents(text, model=None):
    prompt = background + Example1 + Example2 + Example3 + Question1.format(text, EventList)
    if model == None:
        model = chatglm()
    return model.response(prompt)[0]


if __name__ == "__main__":
    text = "近日，研究人员发现SteamHide恶意软件滥用Steam游戏平台进行传播。攻击者通过在Steam平台上更新个人资料头像将恶意软件以加密的形式隐藏其中。Steam平台只是承载恶意文件的工具。下载、解包和执行恶意负载的繁重工作由一个外部组件处理，该组件访问一个Steam配置文件上的图像。"
    print(IdentifyEvents(text))