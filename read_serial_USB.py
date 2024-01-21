import serial

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    data = ser.readline().decode('ascii')
    #temp1, temp2, temp3, temp4 = data.split(",")
    print(data)
    #print(temp1, temp2, temp3, temp4)