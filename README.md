# iosxe-secured-port

This script covers the following scenario: The customer doesn't have ISE and wants to add an extra layer of security for switch ports.
The customer has the following challange: There are people who unplug APs from the switch and plug their devices.
I managed to create a script using the guestshell available on IOS-XE switches.

Steps in order to implement this feature.
1. Enable iox service - link: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/guest_shell.html
<img width="819" alt="image" src="https://github.com/CozmaSerban/iosxe-secured-port/assets/10424327/d5d6179a-6db1-4c26-84d5-36641f2fd119">
2. Enable guestshell container - link: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/guest_shell.html
<img width="1110" alt="image" src="https://github.com/CozmaSerban/iosxe-secured-port/assets/10424327/ade71cdc-e1bf-4fc1-9fbc-ac55a777712f">
3. Copy the script to the containter.
4. Create the EEM Applet

Useful commands:

Turn on interface: guestshell run python3 app.py noshut GigabitEthernet 1/0/1
Turn off interface: guestshell run python3 app.py GigabitEthernet 1/0/1

