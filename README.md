# Vehicle

# I. Description:
Project of remote control of an electric vehicle from a PC.
The control panel was written under Linux operating system in Python.

- PC:
  The control panel that sends a percentage fill to the vehicle that controls the speed of the engines.
  The control panel receives the angular position from the vehicle. Everything is displayed in the control window.
  The control panel allows user to connect to the vehicle via Bluetooth and UART.

- Vehicle:
  The device that controls the engines and sends IMU measurements to the computer is Beagle Bone Blue.
  The device is battery-powered.

- Tests:
  A project testing vehicle functionality using mocking technology.

# II. Structure:
- Common,
- Control Panel,
- Vehicle,
- Tests.

# III. Configuration:
- Ubuntu 20.04.6 LTS,
- Python 3.8,
- bluetooth,
- RCPY on device,
- Flash image with armhf-2020-04-06-4gb.img.xz,
  - Balena Etcher,
  - https://docs.beagleboard.org/latest/boards/beaglebone/blue/flashing-firmware.html.
- Extending BBB partition
  - https://elinux.org/Beagleboard:Expanding_File_System_Partition_On_A_microSD
- Establish Wifi connection
  - https://www.fis.gatech.edu/how-to-configure-bbw-wifi/
  - https://github.com/beagleboard/beaglebone-blue/wiki/Accessories#Radio_remotes

Both PC and device need have configured bluetooth for data exchange.

# IV. Tips:
- Client connects to the server knowing its MAC address,
- If the server(BBB) selects a port other than 1 when starting, you must either change it in the client(Control Panel) or reset the device,
- On Device go to Vehicle folder then execute sudo -E python3 ./Vehicle/Main.py,
- Bluetooth fix no advertisable device
  - https://www.youtube.com/watch?v=vpyQooUksBk/etc/systemd/system/bluetooth.target.wants/bluetooth.service add -C,
- Bluettoth Sap error
  - https://citadel.tistory.com/391
  - nano /etc/systemd/system/bluetooth.target.wants/bluetooth.service
    change to ExecStart=/usr/lib/bluetooth/bluetoothd --noplugin=sap
- Commands for bluetooth refresh:
  - sudo systemctl stop bluetooth
  - sudo systemctl disable bluetooth
  - sudo systemctl enable bluetooth
  - sudo systemctl start bluetooth
  - sudo hciconfig hci0 piscan
- Example of establishing bluetooth connection manually
  - https://www.baeldung.com/linux/bluetooth-via-terminal
  - https://bbs.archlinux.org/viewtopic.php?id=126603
- Interfaces:
  Usb/Uart:
  - ssh debian@192.168.6.2
  - ssh debian@192.168.7.2

  Wifi
  - ssh debian@192.168.1.3
  - ssh debian@beaglebone.local