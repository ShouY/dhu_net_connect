# -*- coding: utf-8 -*-
#
#   处理掉线的情况
#       因为与服务时间不同步,实际断网时间可能有出入。因此在一段时间内监测网络连接
#

from dhu_connect import try_connect, test_connection, cnc_log, parse
import time


if __name__ == "__main__":
    data = parse()
    cnc_log.info("guarding network connecting")
    for i in range(100):
        if not test_connection():
            cnc_log.info("dhu campus network disconnect")
            try_connect(**data)
        time.sleep(5)
    cnc_log.info("stop guard network")
