import jieba.posseg as pseg
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_nouns(text):
    words = pseg.cut(text)  # 使用jieba进行分词和词性标注
    nouns = []
    for word, flag in words:
        if flag.startswith('n'):  # 判断词性是否为名词
            nouns.append(word)
    return nouns

def extract_top_nouns(text, top_percentage):
    nouns = extract_nouns(text)
    corpus = [' '.join(nouns)]  # 将名词列表转换为文本语料
    vectorizer = TfidfVectorizer()  # 初始化TF-IDF向量化器
    tfidf_matrix = vectorizer.fit_transform(corpus)  # 计算TF-IDF矩阵
    feature_names = vectorizer.get_feature_names()  # 获取特征词列表
    scores = tfidf_matrix.toarray().flatten()  # 将TF-IDF矩阵转换为一维数组

    # 根据TF-IDF得分排序，并提取前top_percentage的名词
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    num_top_nouns = int(len(scores) * top_percentage)
    top_nouns = [feature_names[idx] for idx in sorted_indices[:num_top_nouns]]

    return top_nouns



if __name__ == "__main__":
# 示例文本
    text = "研究人员近期捕获了一起针对巴基斯坦木尔坦地区武装力量的网络攻击事件，攻击者以木尔坦的罗德兰区基于情报的反恐行动(intelligence-based operation，IBO)报告为诱饵，尝试投递一种变种木马程序MessPrint以控制受害者设备。经分析，该事件的主导者为APT组织Confucius。本次攻击中，Confucius沿用了其常见的诱饵构建模式，通过利用名为“IBO_Lodhran.doc”（罗德兰地区基于情报的行动）以及“US_Dept_of_State_Fund_Allocations_for_Pakistan.doc”（美国国务院对巴基斯坦的资金分配）的诱饵文档，分别针对巴基斯坦的安全部队与外交类政府部门发起鱼叉式网络钓鱼攻击。当上述钓鱼文档中的宏被执行后，文档将向指定目录释放一个名为gist.txt的加密文件，该文件实际上是一种powershell木马，其最终下载名为VERSION.dll的变种木马程序：MessPrint。新版MessPrint木马程序在功能和对抗方面的变化很大，主版本号从2.X.X升级至3.1.0，且其主要功能分为运行日志记录、受害者主机信息上传与命令执行三部分。"

    # 提取名词并计算重要度
    keywords = extract_nouns(text)

    # 输出重要度排名前60%的名词
    for keyword in keywords:
        print(f"keyword: {keyword}")
