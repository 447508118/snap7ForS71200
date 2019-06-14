from time import sleep
import snap7
from snap7.snap7exceptions import Snap7Exception
from snap7.util import *
from snap7.snap7types import *

db = \
"""
DB001 Real 0.0
DB002 Bool 4.0
DB003 Int 6.0
DB004 String 8.0
DB005 Real 264
"""

def connect(device, ip, rack, slot):
    while True:
        # check connection
        if device.get_connected():
            break
        try:
            # attempt connection
            device.connect(ip, rack, slot)
        except:
            pass
        sleep(5)


# def DBRead(dev, db_num, length, dbitems):
#     data = dev.read_area(0x84, db_num, 0, length)

def main():
    s71200 = snap7.client.Client()
    connect(s71200, '192.168.2.110', 0, 1)
    while True:
        try:
            data = s71200.read_area(0x84, 1, 0, 5)
            print(data)
            value = get_real(data, 0)
            value2 = get_bool(data, 4, 0)
            print(value, value2)
            sleep(5)
        except Snap7Exception as e:
            connect(s71200, '192.168.2.110', 0, 1)

if __name__ == '__main__':
    main()