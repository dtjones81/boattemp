import serial
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

