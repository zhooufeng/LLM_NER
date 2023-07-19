import re
import json

def extractJson(text):
    match = re.search(r'{[^{}]+}', text)
    if match:
        json_str = match.group(0)
        return json_str
    else:
        return None
    
def JsonValidate(text):
    try:
        if len(text.replace("{", "")) + 1 == len(text) and len(text.replace("}", "")) + 1 == len(text):
            return True
        return False
    except:
        return False
    
if __name__ == "__main__":
    text = """{
'因果关系': ['研究人员发现透明部落利用外贸主题的链接进行攻击活动样本'],
'顺承关系': ['研究人员发现透明部落使用的RAT既不是其专属木马CrimsonRAT，也不是常用的ObliqueRAT，而是一款简单的RAT，包含屏幕监控、键盘监控、网络传输的功能']}"""
    result = extractJson(text)
    if result:
        print(result)
    else:
        print("未找到 JSON 字符串。")