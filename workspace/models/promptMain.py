from Utils.extractJson import extractJson, JsonValidate, JsonValidate_Detail
from Utils.GetRelationShips import GetRelationShips
from Utils.GetEventType import GetEventType
from Utils.GetEventDetail import GetEventDetail
from configs.pathcfg import Pcfg
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
        detail1 = extractJson(GetEventDetail(reason, reason_type, model))
        detail2 = extractJson(GetEventDetail(result, result_type, model))
        if not JsonValidate_Detail(detail1) or not JsonValidate_Detail(detail2):
            WARNING("大模型输出的事件进行归类和细节分析json格式有误")
            if not JsonValidate_Detail(detail1):
                DEBUG(f"detail1:{detail1}")
            if not JsonValidate_Detail(detail2):
                DEBUG(f"detail1:{detail2}")
            raise NotImplementedError
        relationJson["因果关系"][pos] = {
            "原因": {
                "事件类型": reason_type,
                "事件细节": json.loads(detail1),
                "事件描述": reason
            },
            "结果": {
                "事件类型": result_type,
                "事件细节": json.loads(detail2),
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
        detail1 = extractJson(GetEventDetail(reason, reason_type, model))
        detail2 = extractJson(GetEventDetail(result, result_type, model))
        if not JsonValidate_Detail(detail1) or not JsonValidate_Detail(detail2):
            WARNING("大模型输出的事件进行归类和细节分析json格式有误")
            raise NotImplementedError
        relationJson["顺承关系"][pos] = {
            "前一事件": {
                "事件类型": reason_type,
                "事件细节": json.loads(detail1),
                "事件描述": reason
            },
            "后一事件": {
                "事件类型": result_type,
                "事件细节": json.loads(detail2),
                "事件描述": result
            }
        }
        pos += 1
    INFO("事件归类和细节分析成功")
    return relationJson


def process(Text, model):
    cnt = 0
    maxcnt = Pcfg.maxRework
    while cnt < maxcnt:
        cnt += 1
        try:
            INFO(f"尝试对输入文本进行事件抽取({cnt}/{maxcnt}次)")
            relation = GetRelationShips(Text, model)
            # DEBUG(f"relation from LLM:{relation}")
            relationJson = extractJson(relation)
            # DEBUG(f"relationJson from LLM:{relationJson}")
            relationJson = relationJson if JsonValidate(relationJson) else 'Json Invalidate'
            if not JsonValidate(relationJson):
                WARNING("大模型输出的json格式有误")
                continue
            else:
                INFO("成功得到事件关系json")
            try:
                return detail(relationJson, model)
            except:
                WARNING("大模型事件细节分析有误")
                continue
        except Exception as e:
            WARNING("大模型输出的json格式有误")
            continue
    return -1

if __name__ == "__main__":
    text = "卢卡申科接着说：“热舒夫对他们来说是不可接受的。他们在阿尔捷莫夫斯克郊区作战时，他们知道（乌克兰的）军车来自哪里，他们由此印象深刻：热舒夫是我们的麻烦。当然，正如我们一致同意的，我把他们安顿在了白俄罗斯中部，我不想重新部署他们，因为他们现在精神有些低落……”"
    print(process(text))