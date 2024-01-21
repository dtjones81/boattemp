import serial

ACCESS_KEY = "ist_qmyWQ3Le1sa6O0QKhYy-OBv81MmfytIt"
BUCKET_KEY = "8VGBGWUN74JH"
BUCKET_NAME = "MonitorIOT"
API_ENDPOINT = "https://groker.init.st/api/events?accessKey=ist_qmyWQ3Le1sa6O0QKhYy-OBv81MmfytIt&bucketKey=8VGBGWUN74JH"
base_url = API_ENDPOINT

ser = serial.Serial('COM3', 9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

try: 
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('ascii')
            final_url = base_url + data
            print(data)
            print(final_url)
            final_url =""
except KeyboardInterrupt:
   print("Exiting...")
finally:
  ser.close()

    