import serial
import time

# Open serial connection to OEM719
ser = serial.Serial(
    port='/dev/ttyAMA0',  # Adjust this to your serial port
    baudrate=115200,       # Adjust if you changed the baudrate on OEM719
    timeout=1
)

def send_command(cmd):
    full_cmd = cmd + '\r'
    ser.write(full_cmd.encode('ascii'))
    print("Command sent:", cmd)
    time.sleep(1)  # wait for response
    while ser.in_waiting:
        response = ser.readline().decode('ascii', errors='ignore').strip()
        print("Response:", response)

# Send LOG command (examples)
# send_command('UNLOGALL')
# send_command("log gprmc ontime 1")  # Start logging GPRMC sentences
# Send SAVECONFIG command to save the config

command = input("Enter command (or 'exit' to quit): ")
if command.lower() == 'exit':
    print("Exiting...")
else:
    send_command(command)

ser.close()
