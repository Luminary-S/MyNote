#! /usr/bin/python3
# -*- coding: utf-8 -*-
#need change udev 
'''
USBHID device read and write class, 
and inheritting from USBHID, Trackball class 

main function:
1. display incremental and absolute values of x and y
2. show the trajectory when pressing ctrl+c

ref: 
1. int to bytes and bytes to int(python3.*) https://www.pynote.net/archives/1383 and python 2.7: https://www.delftstack.com/howto/python/how-to-convert-bytes-to-integers/
2. access usb without sudo, udev change method: https://elinux.org/Accessing_Devices_without_Sudo
3. mouse and keyboard data protocol : https://www.cnblogs.com/vonly/p/7403823.html
4. hid api reference: https://github.com/libusb/hidapi (c version) and  https://github.com/trezor/cython-hidapi (python version, for docs pls using sphinx to automatically generate)

note:
1. hid package from pip install hidapi, 
2. take care of pip and python version, seen in `python -V` and `pip -V`, test in python3.6 and python2.7
'''
__author__ = "sgl"
__version__ = "v1.0"

import hid
import time
import sys
import struct
import matplotlib.pyplot as plt 

class USBHID(object):
    '''
    USB hid device class 
    '''
    def __init__(self, vid, pid):
        '''
        Initialize a USBHID

        : param alive: whether the device is opened
        : param handle: the hid got device
        : param size: previous setting reading buff size

        note:
        vid(idVendor) and pid(idProduct) can be seen by command `lsusb -vvv`
        '''
        self.alive = False
        self.handle = None
        self.size = 4
        self.vid = vid
        self.pid = pid

    def find(self, vid, pid):
        # for device_dict in hid.enumerate():
        #     keys = list(device_dict.keys())
        #     keys.sort()
        #     for key in keys:
        #         print("%s : %s" % (key, device_dict[key]))
        device_list = hid.enumerate(vid, pid)
        # print(device_list)
        return device_list

    def set_device( self, id=0 ):
        self.dev = self.find( vid = self.vid, pid = self.pid )
        device = self.dev[id]
        return device

    def start( self, device ):
        '''
        start and open the device

        :param device: the specific hid device information dict
        '''
        # self.dev = self.find(idVendor=self.vid, idProduct=self.pid)
        # device = self.dev[0]
        if device != None:
            self.handle = hid.device()
            self.handle.open_path( device['path'] )

            print("Manufacturer: %s" % self.handle.get_manufacturer_string())
            print("Product: %s" % self.handle.get_product_string())
            print("Serial No: %s" % self.handle.get_serial_number_string())
            # self.ep_in = self.dev[0][(0,0)][0].bEndpointAddress
            # self.ep_out = self.dev[0][(0,0)][1].bEndpointAddress
            # self.size = self.dev[0][(0,0)][1].wMaxPacketSize
            # enable non-blocking mode
            self.handle.set_nonblocking(1)
        # self.open()
            self.alive = True

    def stop(self):
        '''
        close device, if needed, release handle
        '''
        self.alive = False
        if self.handle:
            self.handle.close()

    # def open(self):
    #     '''
    #     open usb device
    #     '''
    #     busses = usb.busses()
    #     for bus in busses:
    #         devices = bus.devices
    #         for device in devices:
    #             if device.idVendor == self.vid and device.idProduct == self.pid:
    #                 print("find it")
    #                 self.handle = device.open()
    #                 # Attempt to remove other drivers using this device.
    #                 if self.dev.is_kernel_driver_active(0):
    #                     try:
    #                         self.handle.detachKernelDriver(0)
    #                     except Exception as e:
    #                         self.alive = False
    #                 try:
    #                     self.handle.claimInterface(0)
    #                 except Exception as e:
    #                     self.alive = False

    def read(self, size=4, timeout=0):
        '''
        read data from usb port

        :param size: read byte number, 1byte=8bit, 4byte is short int
        :param timeout: read timeout setting        
        '''
        if size >= self.size:
            self.size = size

        # if self.handle:
            # data = self.handle.interruptRead(self.ep_in, self.size, timeout)
        # x = 0
        # y = 0
        try:
            d = self.handle.read( self.size )
            # print("data:", d)
            if d:
                # print("data:", d)
                return d
            else:
                print("no data read out.")
            
            # return x,y
        except:
            print("read data error!")
            # return 0,0

    def write(self, send_list, timeout=1000):
        '''
        send data to usb

        :param send_list: send data list, if in int, it will send it by byte

        example: [0, 63, 35, 35] + [0] * 61
        '''
        if self.handle:
            self.handle.write(send_list, timeout)
            # return bytes_num

class Trackball(USBHID):
    '''
    Trackball class 
    '''
    def __init__(self, vid=0x04b4, pid=0x6370):
        '''
        set the trackball inherit from the USBHID, vid and pid is setted

        Initialize a trackball, vid and pid can be seen by command `lsusb -vvv`
        '''
        super(Trackball,self).__init__(vid, pid)

    def data_init(self):
        '''
        initial data of mouse: position and incremental position, list is used for plotting
        '''
        self.x = 0
        self.y = 0
        self.d_x = 0
        self.d_y = 0
        self.x_list= []
        self.y_list = []
    
    def parse_data(self, d):
        '''
        parse the raw data from usb port and get the incremental x and y 
        x positive: to usb wire
        y positive: take the device , wire down, positive is right. 
        here, get int number from 

        :param d: raw data from port reading

        note:
        mouse send complement code to pc, 4 bytes
        byte1 and byte4: useless here about roller and btns, if needed, refer to reference 3 
        byte2: x, complement code, signed int
        byte3: y, complement code, signed int

        1 means returning bytes object of length 1, which is 1 byte
        *big* means front 4 bits is bigger than back 4 bits, if inverse, change to *little *
        signed means signed int or not 
        '''
        d_x = 0
        d_y = 0
        if sys.version_info.major == 3:
            byte_data = [ i.to_bytes(1, 'big', signed=False) for i in d ]
                # print("---byte data:", byte_data)
            int_data = [ int.from_bytes( i , 'big', signed=True) for i in byte_data ]
            d_x = int_data[1]
            d_y = int_data[2]
        elif sys.version_info.major == 2:
            # print("raw data:", d)
            byte_data = [ struct.pack('>B', i) for i in d ]
            int_data = [ struct.unpack( '>b', i )[0] for i in byte_data ] # big-endian, short integer
            # print(byte_data)
            # print(int_data)
            d_x = int_data[1]
            d_y = int_data[2]            
        return d_x,d_y

    def update(self):
        '''
        program inside the loop
        '''
        d = self.read(4)

        d_x = 0
        d_y = 0
        if d:
            d_x,d_y = self.parse_data(d)
        self.d_x = d_x
        self.d_y = d_y
        self.x = self.x + d_x
        self.y = self.y + d_y
        self.x_list.append(self.x)
        self.y_list.append(self.y)
    
    def run(self):
        '''
        main 

        Note:
        device 0 is the first device matching the vid and pid
        _TIME sets the loop frequency
        '''        
        # device_dict = device
        device = self.set_device(0)  # first device for vid and pid device

        try: 
            self.start( device )

            self.data_init()

            #------ros change part starts -----------
            _TIME = 1.0/100
            print("Read the data")
            while True:

                self.update()
                print("delta data---- x: %d, y: %d;  abs data---- x: %d, y: %d." %(self.d_x,self.d_y,self.x,self.y))
                time.sleep(_TIME)
            #------ros change part ends-----------


            print("Closing the device")
            self.stop()           
        except IOError as ex:
            print(ex)
            print("You probably don't have the hard-coded device.")
            print("Update the h.open() line in this script with the one")
            print("from the enumeration list output above and try again.")

        except KeyboardInterrupt:
            self.plot_data()
            print("break")

        print("Done")

    def plot_data(self):
        '''
        plot x,y trajectory

        note:
        1. subplot 1,2,1: col 1, row 2, first row
        '''
        plt.figure(1)
        plt.title("trackball trajectory")
        plt.plot( self.x_list, self.y_list, color="r", label="real" )
        plt.legend()

        plt.figure(2)
        plt.title("trackball trajectory of x and y direction")

        plt.subplot(1,2,1)  
        plt.plot( self.x_list, label="x direction" )

        plt.subplot(1,2,2)
        plt.plot( self.y_list, label="y direction" )
        plt.show()

if __name__ == '__main__':

    tb = Trackball()

    tb.run()

