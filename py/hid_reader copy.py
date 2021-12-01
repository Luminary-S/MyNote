#! /usr/bin/python3
# -*- coding: utf-8 -*-
#need change udev 
'''
usb hid device read and write class
ref: 
1. int to bytes and bytes to int https://www.pynote.net/archives/1383
2. access usb without sudo, udev change method: https://elinux.org/Accessing_Devices_without_Sudo
3. mouse and keyboard data protocol : https://www.cnblogs.com/vonly/p/7403823.html
4. hid api reference: https://github.com/libusb/hidapi (c version) and  https://github.com/trezor/cython-hidapi (python version, for docs pls using sphinx to automatically generate)
'''
__author__ = "sgl"
__version__ = "v1.0"

import hid
import time



# def read_from_hid(dev, timeout):
#     try:
#         # read a maximum of 8 bytes from the device, with a user specified timeout
#         data = dev.read(8, timeout)
#     except IOError as e:
#         print ('Error reading response: {}'.format(e))
#         return None

#     byte_str = ''.join(chr(n) for n in data[1:]) # construct a string out of the read values, starting from the 2nd byte

#     result_str = byte_str.split('\x00',1)[0] # remove the trailing null '\x00' characters

#     if len(result_str) == 0:
#         return None

#     return result_str

VENDOR_ID = 0x04b4 # OnTrak Control Systems Inc. vendor ID
PRODUCT_ID = 0x6370 # ADU200 Device product name - change this to match your product
# VENDOR_ID = 0x046d # OnTrak Control Systems Inc. vendor ID
# PRODUCT_ID = 0xc077 # ADU200 Device product name - change this to match your product
device_list = hid.enumerate(VENDOR_ID, PRODUCT_ID)
print(device_list)

# device = hid.device()
# print(device)
# # device.open(VENDOR_ID, PRODUCT_ID)
# device_dict = (device in device_list if device['usage'] == '0').next()
device_dict = device_list[0]
# device = hid.device()
# device.open_path(device_dict['path']) #Open from path
# print('Connected to trackball {}\n'.format(PRODUCT_ID))

# for device_dict in hid.enumerate():
#     keys = list(device_dict.keys())
#     keys.sort()
#     for key in keys:
#         print("%s : %s" % (key, device_dict[key]))
#     print()
x_list = []
y_list = []
_TIME = 1.0/100
try:
    print("Opening the device")

    h = hid.device()
    # h.open(PRODUCT_ID, VENDOR_ID)  # TREZOR VendorID/ProductID
    h.open_path(device_dict['path'])

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    # print("Write the data")
    # h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    # time.sleep(0.05)

    # read back the answer
    print("Read the data")
    # num = 10
    x = 0
    y = 0
    d_x = 0
    d_y = 0
    while True:
        
        d = h.read(5)
        # print("data:", d)
        if d:
            # print("data:", d)
        # bu_data = [ ~(i-1) for i in d ]
        # print("---bu data:", bu_data)
            byte_data = [ i.to_bytes(1, 'big', signed=False) for i in d ]
        # print("---byte data:", byte_data)
            int_data = [ int.from_bytes( i , 'big', signed=True) for i in byte_data ]
            
            d_x = int_data[1]
            d_y = int_data[2]
        # num -= 1
        else:
            d_x = 0
            d_y = 0
        x += d_x
        y += d_y
        print("delta data---- x: %d, y: %d;  abs data---- x: %d, y: %d." %(d_x,d_y,x,y))
        # if d:
        #     print(d)
        # else:
        #     break
        time.sleep(_TIME)
    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")