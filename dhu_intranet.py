from http import client

import requests


def test_connection(test_url: str = "baidu.com"):
    """测试是否连接到网络"""
    conn = client.HTTPConnection(test_url)
    conn.request("GET", "/")
    return conn.getresponse().getcode() == 200


def connect(username: str, password: str):
    """ 连接校园网

    Args:
        username: 用户学号
        password: 校园网账号的密码

    Returns:
        是否连接成功。
    """
    config = {
        'username': username,
        'password': password,
        'savePWD': 'on'
    }
    sess = requests.Session()
    sess.get("http://msfttestconnect.com")
    if not sess.verify:
        return False

    sess.cookies.set("pwd", "")
    sess.cookies.set("username", config['username'])
    sess.cookies.set("smartdot", "")
    resp = sess.post("https://portalnew2.dhu.edu.cn/post.php", data=config)
    return resp.ok
