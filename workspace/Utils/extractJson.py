import re
import json
try:
    from Utils.debugformat import INFO, DEBUG, WARNING
except:
    from debugformat import INFO, DEBUG, WARNING

def extractJson(text):
    match = re.search(r'{[^{}]+}', text)
    if match:
        json_str = match.group(0)
        return json_str
    else:
        return None
"""  
def JsonValidate(text):
    try:
        if len(text.replace("{", "")) + 1 == len(text) and len(text.replace("}", "")) + 1 == len(text):
            return True
        return False
    except:
        return False
"""


def JsonValidate(json_str):
    try:
        # DEBUG(json_str)
        json_object = json.loads(json_str)
        if "因果关系" not in json_object or "顺承关系" not in json_object:
            return False
    except json.JSONDecodeError:
        return False
    return True


def JsonValidate_Detail(json_str):
    try:
        # DEBUG(json_str)
        json_object = json.loads(json_str)
    except Exception as e:
        DEBUG(e)
        # raise e
        return False
    return True


if __name__ == "__main__":
    text = """{"攻击对象": "SteamHide恶意软件", "攻击者": "未知", "攻击手段": "滥用Steam游戏平台进行传播", "攻击工具": "None"}"""
    print(JsonValidate_Detail(text))
    result = extractJson(text)
    if result:
        print(result)
    else:
        print("未找到 JSON 字符串。")