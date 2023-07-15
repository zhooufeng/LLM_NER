from load_model import chatglm

background = """
我希望你能够以一名语言学家的身份完成我的任务。

首先我会给你一段文字，然后我会给你一个该段文字中发生过的事件。
你需要做的事情是，提取出这些事件之间的因果关系和顺承关系，以json格式输出。
"""
Example1 = """
例子1：

文字：研究人员近期捕获了一起针对巴基斯坦木尔坦地区武装力量的网络攻击事件，攻击者以木尔坦的罗德兰区基于情报的反恐行动(intelligence-based operation，IBO)报告为诱饵，尝试投递一种变种木马程序MessPrint以控制受害者设备。

事件类型：攻击事件，恶意软件事件

输出：{}
""".format({"因果关系": "无", "顺承关系": "恶意软件事件->攻击事件"})
Example2 = """
例子2：

文字：近日，DFIR研究人员检测到一起利用WebLogic远程代码执行漏洞(CVE-2020–14882)入侵并植入XMRig矿机的攻击活动。此次活动中，攻击者通过利用WebLogic漏洞入侵主机，执行PowerShell指令从远程服务器下载PowerShell脚本，获取后续组件加载XMRig。研究人员发现，攻击者利用netstat来查找是否有正在使用挖矿相关端口的进程，还禁用了防火墙规则以确保与矿池的稳定连接。

事件类型：攻击事件，漏洞事件

输出：{}
""".format({"因果关系": "漏洞事件->攻击事件", "顺承关系": "未知"})
Question1 = """
问题1：

文字：{}

事件类型：{}

输出：
"""

def GetRelationShips(text, EventType, model=None):
    prompt = background + Example1 + Example2 + Question1.format(text, EventType)
    if model == None:
        model = chatglm()
    return model.response(prompt)[0]


if __name__ == "__main__":
    text = "近日，研究人员发现SteamHide恶意软件滥用Steam游戏平台进行传播。攻击者通过在Steam平台上更新个人资料头像将恶意软件以加密的形式隐藏其中。Steam平台只是承载恶意文件的工具。下载、解包和执行恶意负载的繁重工作由一个外部组件处理，该组件访问一个Steam配置文件上的图像。"
    EventType = "漏洞事件，恶意软件事件，社交媒体事件"
    print(GetRelationShips(text, EventType))