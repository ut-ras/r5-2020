# r5-2020

See the [wiki](https://github.com/ut-ras/r5-2020/wiki).

# SSHing into the raspberry pi
The pi currently connects my (Matthew's) hotspot, since connecting to the UT network is annoying and less safe.

You can modify which network the pi will attempt to connect to on startup by taking the `wpa_supplicant.conf` and modifying the following:
`ssid="the name of your network"`
`psk="the password of your network"`

You can do this by editing from the sdcard manually or while ssh'd to the rpi.

To connect to the raspberry pi, use the following command while **connected to the same network**:
`ssh pi@raspberrypi.local`

The default password is *raspberry*.

(Tutorial source](https://medium.com/@nikosmouroutis/how-to-setup-your-raspberry-pi-and-connect-to-it-through-ssh-and-your-local-wifi-ac53d3839be9)