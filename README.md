# olhogrego_raspberrypi

## Environment
- raspberry pi 2 b+
- noobs 2.0
- raspebian jessi with pixel

## Dependencies
- bluez python-bluez:
		* reference: http://blog.davidvassallo.me/2014/05/11/android-linux-raspberry-pi-bluetooth-communication/
		$ sudo apt-get install bluez python-bluez
		add the following to /etc/bluetooth/main.conf:
		DisablePlugins = pnat
		sudo hciconfig hci0 piscan [make your device discover-able]
		sudo hciconfig hci0 name 'Device Name' [change your device name to something else you fancy]
		
		