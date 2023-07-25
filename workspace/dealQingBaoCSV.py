from main import Runner
import pandas as pd
from configs.pathcfg import Pcfg

qingbaoCSV = pd.read_csv(Pcfg.csvPath+"/qingbao.csv", on_bad_lines='skip')
print(qingbaoCSV.head())
A = Runner()

text = []
for i in qingbaoCSV['content']:
    text.append(i)

A.RunInBatches(TextList=text, savePath=Pcfg.jsonPath + "/qingbao.json")
