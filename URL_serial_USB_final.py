import serial
import requests

ACCESS_KEY = "ist_qmyWQ3Le1sa6O0QKhYy-OBv81MmfytIt"
BUCKET_KEY = "8VGBGWUN74JH"
BUCKET_NAME = "MonitorIOT"
API_ENDPOINT = "https://groker.init.st/api/events?accessKey=ist_qmyWQ3Le1sa6O0QKhYy-OBv81MmfytIt&bucketKey=8VGBGWUN74JH"
base_url = API_ENDPOINT
file_name = "responses.json"

ser = serial.Serial('COM3', 9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

try: 
    while True:
        if ser.in_waiting > 0:  #looks for data from USB
            data = ser.readline().decode('ascii')  #reads the USB port for data
            final_url = base_url + data  #builds the URL
            response = requests.get(final_url)  #GET to send the data
            if response.status_code == 204:  #logs the status code if GET fails
               with open(file_name, "ab") as file:  #appending to log file
                  file.write(response.content)
               print("file appended successfully")   
            else:
               print("Request failed with status code:", response.status_code)
            final_url =""  #clears the URL for next data send
except KeyboardInterrupt:
   print("Exiting...")
finally:
  ser.close()

    