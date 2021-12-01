#! /usr/bin/python3
# -*- coding: utf-8 -*-
#need change udev 
'''
linux下使用的usb设备通讯帮助类
'''
__author__ = "sgl"
__version__ = "v1.0"


import threading
import usb.util
import usb.core
import time

print("1")

class usbHelper(object):
    def __init__(self, vid, pid):
        self.alive = False
        self.handle = None
        self.size = 64
        self.vid = vid
        self.pid = pid

    def start(self):
        '''
        开始，打开usb设备
        '''
        self.dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0,0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0,0)][1].bEndpointAddress
            self.size = self.dev[0][(0,0)][1].wMaxPacketSize
        self.open()
        self.alive = True

    def stop(self):
        '''
        停止，关闭usb设备，释放接口
        '''
        self.alive = False
        if self.handle:
            self.handle.releaseInterface()

    def open(self):
        '''
        打开usb设备
        '''
        busses = usb.busses()
        for bus in busses:
            devices = bus.devices
            for device in devices:
                if device.idVendor == self.vid and device.idProduct == self.pid:
                    print("find it")
                    self.handle = device.open()
                    # Attempt to remove other drivers using this device.
                    if self.dev.is_kernel_driver_active(0):
                        try:
                            self.handle.detachKernelDriver(0)
                        except Exception as e:
                            self.alive = False
                    try:
                        self.handle.claimInterface(0)
                    except Exception as e:
                        self.alive = False

    def read(self, size=64, timeout=0):
        '''
        读取usb设备发过来的数据
        '''
        if size >= self.size:
            self.size = size

        if self.handle:
            data = self.handle.interruptRead(self.ep_in, self.size, timeout)

        try:
            print("Raw data: {0}".format(data))
            data_list = data.tolist()
            # print(data_list)
            return data_list
        except:
            return list()

    def write(self, send_list, timeout=1000):
        '''
        发送数据给usb设备
        '''
        if self.handle:
            bytes_num = self.handle.interruptWrite(self.ep_out, send_list, timeout)
            return bytes_num

if __name__ == '__main__':

    dev = usbHelper(0x04b4, 0x6370)

    dev.start()

    send_list = [0xAA for i in range(64)]
    dev.write(send_list)
    # time.sleep(0.25)
    while True:
        try:
            mylist = dev.read()
            print(mylist)
            if mylist[1] == 0x02:
                break
        except:
            dev.stop()
            break
    dev.stop()