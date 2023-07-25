import json
with open("CEC.json", "r", encoding='utf-8') as f:
    res = json.load(f)


sum = []
for i in res:
    sum.append(res[i]['content'].replace("\n", ""))

with open("CEC_raw.txt", "w", encoding='utf-8') as f:
    for i in sum:
        f.write(i + '\n')