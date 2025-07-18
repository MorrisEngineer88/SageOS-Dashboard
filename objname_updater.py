# objname_updater.py
import serial
from main import format_display_data

def send_to_nextion(data, port="/dev/ttyUSB0", baudrate=9600):
    """Sends formatted data to Nextion display via serial."""
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        for key, value in data.items():
            command = f"{key}.txt=\"{value}\""
            ser.write(command.encode('utf-8') + b'\xff\xff\xff')
        ser.close()
    except Exception as e:
        print(f"Error sending to Nextion: {e}")

if __name__ == "__main__":
    display_data = format_display_data()
    send_to_nextion(display_data)
