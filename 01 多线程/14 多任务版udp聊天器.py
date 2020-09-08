# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/4 15:51
import socket
import threading


def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        # 1. 接收数据
        msg = udp_socket.recvfrom(1024)

        # 2. 解码
        recv_ip = msg[1]
        msg = msg[0].decode("gbk")

        # 3. 显示接收到的数据
        print(">>>%s:%s" % (recv_ip, msg))


def send_msg(udp_socket, dest_ip, dest_port):
    """获取键盘数据，并将其发送给对方"""
    while True:
        # 3. 从键盘输入数据
        msg = input("请输入要发送的数据:")
        # 4. 发送数据
        udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成udp聊天器的整体控制"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """绑定ip和port"""
    udp_socket.bind(("", 7788))

    # 1. 输入对方的ip地址
    dest_ip = input("请输入对方的ip地址:")

    # 2. 输入对方的端口号
    try:
        dest_port = int(input("请输入对方的端口号:"))
    except Exception as e:
        dest_port = None
        print(e)

    t1 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t2 = threading.Thread(target=recv_msg, args=(udp_socket, ))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
