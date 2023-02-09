# unifi_autoinform
Simple script for setting the "set-inform" for devices on the local subnet.  This will attempt to login to any devices on the designated subnet that have port 22 open and accept the default UniFi credentials.  Upon successful login it will then point those devices to your designated controller.  You'll want to modify the subnet and inform IP to match your needs.  
