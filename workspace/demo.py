from load_model import chatglm
import pprint
model = chatglm()
pprint.pprint(model.response("根据百度百科的定义，威胁情报旨在为面临威胁的资产主体(通常为资产所属企业或机构)提供全面的、准确的、与其相关的、并且能够执行和决策的知识和信息。那么在一份威胁情报中，可能会出现的事件类型有哪些？"))