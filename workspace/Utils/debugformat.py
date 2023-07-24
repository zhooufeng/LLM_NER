import time


def calcTime():
    current_timestamp = time.time()
    current_time_struct = time.localtime(current_timestamp)
    current_date = time.strftime("%Y-%m-%d", current_time_struct)
    current_time = time.strftime("%H:%M:%S", current_time_struct)
    return f"{current_date}\t{current_time}"  # 在日期和时间之间插入制表符


def INFO(TextIn):
    print(f"[INFO]\t{calcTime()}: {TextIn}")  # 使用制表符来对齐


def DEBUG(TextIn):
    print(f"[DEBUG]\t{calcTime()}: {TextIn}")  # 使用制表符来对齐


def WARNING(TextIn):
    print(f"[WARNING]\t{calcTime()}: {TextIn}")  # 使用制表符来对齐


if __name__ == '__main__':
    INFO("load model")
    DEBUG("load model")
    WARNING("load model")
