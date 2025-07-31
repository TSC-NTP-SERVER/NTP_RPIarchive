import serial

# Open the serial port connected to OEM719 (AMA0)
ser = serial.Serial(
    port='/dev/ttyAMA0',   # UART port
    baudrate=115200,         # Default for OEM719 unless changed
    timeout=1              # 1 second timeout
)

print("Listening for NMEA data on /dev/ttyAMA0...")

try:
    while True:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        if line.startswith('$'):  # NMEA sentences start with $
            print("NMEA:", line)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()