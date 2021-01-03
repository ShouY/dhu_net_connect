# -*- coding: utf-8 -*-
#
#   处理掉线的情况
#       因为与服务时间不同步,实际断网时间可能有出入。因此在一段时间内监测网络连接
#

from dhu_connect import try_connect, test_connection, cnc_log
import time


def connect():
    try_connect('Username', 'password', 10, 2)


if __name__ == "__main__":
    for i in range(100):
        if not test_connection():
            cnc_log.info("dhu campus network disconnect")
            connect()
        time.sleep(5)
