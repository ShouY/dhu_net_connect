# -*- coding: utf-8 -*-
#
# 自动连接东华大学校园网
#
# Usage:
#   参见`parse`方法
#
# Example:
#   1. 命令行启动。将下列命令行添加到定时任务：
#       python3 [文件路径]\dhu_connect.py 校园网账号 校园网密码 10 2
#   脚本会重试10次连接（最多11次），每次暂停2秒，直到成功连接或者重试次数用尽
#
#   2. 脚本调用。
#       ```
#       from dhu_connect import try_connect
#       try_connect(校园网账号,密码,10,2)
#       ```

import logging
import sys
import time

from dhu_intranet import connect, test_connection

# DHU Campus Network Connect logger
cnc_log = logging.getLogger("dhu CNC")
cnc_log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# 添加控制台日志
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)
cnc_log.addHandler(stream_handler)
# 添加文件日志
file_handler = logging.FileHandler(
    "./dhu_cnc.log", 'a+', encoding='utf-8', delay=False)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
cnc_log.addHandler(file_handler)


def parse():
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        print(
            "Usage: dhu_connect.py username password [retry_times [interval]]")
        return

    data = {
        'username': sys.argv[1],
        'password': sys.argv[2],
        'retry': 0,
        'interval': 1.0
    }
    try:
        if len(sys.argv) >= 4:
            retry = int(sys.argv[3])
            if retry < 1:
                print("retry times less then 1")
                return
            else:
                data['retry'] = retry
        if len(sys.argv) >= 5:
            interval = float(sys.argv[4])
            if interval < 0:
                print('retry interval less than 0')
                return
            else:
                data['interval'] = interval
    except ValueError:
        return
    return data


def try_connect(username: str, password: str, retry: int, interval: float):
    connect_times = 0
    connected = test_connection()

    while not connected and connect_times < retry:
        connect_times += 1

        cnc_log.info("connecting to campus network: {}".format(username))
        if not connect(username=username, password=password):
            cnc_log.warning("connect error")
        time.sleep(interval)
        connected = test_connection()

    result = "sussess" if connected else "fail"
    cnc_log.info(f"connected {result} after {connect_times} times try")


if __name__ == "__main__":
    cnc_log.info("start connect")
    data = parse()
    if not data:
        cnc_log.error("argument mistake:{}".format(sys.argv))
        exit(0)

    user = data['username']
    password = data['password']
    retry = data['retry'] + 1  # 包含最开始的一次连接
    interval = data['interval']
    try_connect(user, password, retry, interval)
