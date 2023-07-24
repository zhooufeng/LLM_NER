import time
import os
import inspect


def calcTime():
    current_timestamp = time.time()
    current_time_struct = time.localtime(current_timestamp)
    current_date = time.strftime("%Y-%m-%d", current_time_struct)
    current_time = time.strftime("%H:%M:%S", current_time_struct)
    return f"{current_date}\t{current_time}"


def INFO(TextIn):
    # 获取调用栈信息
    caller_frame = inspect.currentframe().f_back
    caller_filename = inspect.getframeinfo(caller_frame).filename
    caller_lineno = inspect.getframeinfo(caller_frame).lineno
    print(f"[INFO]\tin file {os.path.basename(caller_filename)}(line {caller_lineno})\t{calcTime()}: {TextIn}")


def DEBUG(TextIn):
    caller_frame = inspect.currentframe().f_back
    caller_filename = inspect.getframeinfo(caller_frame).filename
    caller_lineno = inspect.getframeinfo(caller_frame).lineno
    print(f"[DEBUG]\tin file {os.path.basename(caller_filename)}(line {caller_lineno})\t{calcTime()}: {TextIn}")


def WARNING(TextIn):
    caller_frame = inspect.currentframe().f_back
    caller_filename = inspect.getframeinfo(caller_frame).filename
    caller_lineno = inspect.getframeinfo(caller_frame).lineno
    print(f"[WARNING]\tin file {os.path.basename(caller_filename)}(line {caller_lineno})\t{calcTime()}: {TextIn}")


if __name__ == '__main__':
    INFO("load model")
    DEBUG("load model")
    WARNING("load model")
