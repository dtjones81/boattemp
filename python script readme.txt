

#!/usr/bin/python3

import serial

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s
    
    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
reader = ReadLine(ser)
while True:
    print(reader.readline())


## ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
## while True:
##    reading = ser.readline()
##    print(reading)

found in forums, assumes that USB file is created (in /dev) .  If not look for the lsusb output, and then 

lsusb
pi@raspberrypi:~ $ lsusb
Bus 001 Device 002: ID 0584:b022 RATOC System, Inc.
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
sudo modprobe ftdi_sio
 echo "0584 b022" | sudo tee /sys/bus/usb-serial/drivers/ftdi_sio/new_id

Draft script : 

from ISStreamer.Streamer import Streamer

ACCESS_KEY = "ist_z8bWVIVxMa1QdCu24KjLRrn3DcbxVEBc"
BUCKET_KEY = "VA3LASH3VS8P"
BUCKET_NAME = "USB-URL test bucket"
API_ENDPOINT = "https://groker.init.st/api/events?accessKey=ist_z8bWVIVxMa1QdCu24KjLRrn3DcbxVEBc&bucketKey=VA3LASH3VS8P"

# create a Streamer instance
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

# loop until breaks
while True:
    output = ''
    ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)
    while output == '':
        output = ser.readline()  # reads the input
	streamer.log(output)  # sends the data
    print(output) # prints outputs to screen

# flush and close the stream
streamer.flush()