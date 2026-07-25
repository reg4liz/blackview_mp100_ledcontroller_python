# blackview_mp100_ledcontroller_python
Simple python script to control the rgb leds on the case of the blackview mp100 mini pc under linux. Should work under windows with minimal modifications.

Modify b1, b2 and b3 in the script to set the mode, intensity and speed respectively. Set b1 to THEME_OFF to turn leds off.

# Turning the leds off automatically
To make the leds turn off on bootup, set b1 to THEME_OFF and create a systemd service:

1.- Create a systemd service file:
sudo nano /etc/systemd/system/mp100-led-off.service

2.- Edit the systemd service file and paste this inside (change ExecStart with your paths as required):
[Unit]
Description=Turn off Blackview MP100 RGB LEDs
After=multi-user.target serial-getty@ttyUSB0.service

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/user/mp100_led.py
RemainAfterExit=true

[Install]
WantedBy=multi-user.target

3.- Enable and start the service:
sudo systemctl daemon-reload
sudo systemctl enable --now mp100-led-off.service

From that point on the leds should turn off when you log in. If you need them off any earlier you're gonna need to dig into the pc to physically disconnect the leds.
