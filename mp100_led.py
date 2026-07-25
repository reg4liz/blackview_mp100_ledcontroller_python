#!/usr/bin/env python3
import serial
import time

def checksum(b0, b1, b2, b3):
    return (b0 + b1 + b2 + b3) & 0xFF

def set_on_exact(device):
    SIGNATURE_BYTE = 0xFA
    THEME_RAINBOW = 0x01
    THEME_BREATHING = 0x02
    THEME_SOLID = 0x03
    THEME_OFF = 0x04
    THEME_AUTO = 0x05 
    
    b0 = SIGNATURE_BYTE
    b1 = THEME_RAINBOW
    b2 = 0x03  # Intensity (1-5)
    b3 = 0x03  # Speed (1-5)
    b4 = checksum(b0, b1, b2, b3)
    
    buffer_data = bytes([b0, b1, b2, b3, b4])
    print(f"Sending turn-on payload: {buffer_data.hex()}")

    with serial.Serial(device, baudrate=10000, timeout=1) as ser:
        for byte in buffer_data:
            ser.write(bytes([byte]))
            time.sleep(0.005)

if __name__ == '__main__':
    set_on_exact('/dev/ttyUSB0')
