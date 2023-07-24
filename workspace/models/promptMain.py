from Utils.extractJson import extractJson, JsonValidate
from Utils.GetRelationShips import GetRelationShips
from Utils.GetEventType import GetEventType
from Utils.GetEventDetail import GetEventDetail
# from Utils.load_model import chatglm
import json
import os
import sys
from Utils.debugformat import INFO, DEBUG, WARNING
sys.path.append(os.getcwd())


def detail(JsonIn, model):
    INFO("对事件进行归类和细节分析")
    pos = 0
    relationJson = json.loads(JsonIn)
    for item in relationJson["因果关系"]:
        reason = item.split("->")[0]
        result = item.split("->")[1]
        reason_type = GetEventType(reason, model)
        result_type = GetEventType(result, model)
        relationJson["因果关系"][pos] = {
            "原因": {
                "事件类型": reason_type,
                "事件细节": GetEventDetail(reason, reason_type, model),
                "事件描述": reason
            },
            "结果": {
                "事件类型": result_type,
                "事件细节": GetEventDetail(result, result_type, model),
                "事件描述": result
            }
        }
        pos += 1

    pos = 0
    for item in relationJson["顺承关系"]:
        reason = item.split("->")[0]
        result = item.split("->")[1]
        reason_type = GetEventType(reason, model)
        result_type = GetEventType(result, model)
        relationJson["顺承关系"][pos] = {
            "前一事件": {
                "事件类型": reason_type,
                "事件细节": GetEventDetail(reason, reason_type, model),
                "事件描述": reason
            },
            "后一事件": {
                "事件类型": result_type,
                "事件细节": GetEventDetail(result, result_type, model),
                "事件描述": result
            }
        }
        pos += 1
    return relationJson


def process(Text, model):
    INFO("对输入文本进行事件抽取")
    relation = GetRelationShips(Text, model)
    # DEBUG(f"relation from LLM:{relation}")
    relationJson = extractJson(relation)
    relationJson = relationJson if JsonValidate(relationJson) else 'Json Invalidate'
    if not JsonValidate(relationJson):
        WARNING("大模型输出的json格式有误")
        return
    else:
        INFO("成功得到事件关系json")
    try:
        return detail(relationJson, model)
    except Exception as e:
        WARNING("ERROR in function 'detail'")
        raise e

if __name__ == "__main__":
    text = "卢卡申科接着说：“热舒夫对他们来说是不可接受的。他们在阿尔捷莫夫斯克郊区作战时，他们知道（乌克兰的）军车来自哪里，他们由此印象深刻：热舒夫是我们的麻烦。当然，正如我们一致同意的，我把他们安顿在了白俄罗斯中部，我不想重新部署他们，因为他们现在精神有些低落……”"
    print(process(text))