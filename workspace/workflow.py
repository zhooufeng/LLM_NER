import pandas as pd
from Utils.GetRelationShips import GetRelationShips
from Utils.GetEventType import GetEventType
from Utils.GetEventDetail import GetEventDetail
from Utils.load_model import chatglm
from Utils.extractJson import extractJson, JsonValidate
import json
import tqdm


model = chatglm()


def process(Text):
    relation = GetRelationShips(Text, model)
    relationJson = extractJson(relation)
    relationJson = relationJson if JsonValidate(relationJson) else 'Json Invalidate'
    if not JsonValidate(relationJson):
        print("INFO：Json Invalidate")
        return
    
    try:
        pos = 0
        relationJson = json.loads(relationJson)
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
    except Exception as e:
        return f"ERROR:{e}"

if __name__ == "__main__":
    df = pd.read_csv("./qingbao.csv",  on_bad_lines='skip')
    res = []
    for i in df['origin']:
        res.append(i)

    ana_res = []
    for i in tqdm.tqdm(res):
        ana_res.append({"事件描述": i, "事件分析结果": relationJson})
        with open("./analysis_result.json", 'w', encoding='utf-8') as f:
            json.dump(ana_res, f, indent=4)