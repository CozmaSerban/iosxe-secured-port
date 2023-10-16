# iosxe-secured-port

This script covers the following scenario: The customer doesn't have ISE and wants to add an extra layer of security for switch ports.

The customer has the following challange: There are people who unplug APs from the switch and plug their devices.

I created a script using the guestshell available on IOS-XE switches. As soon as an internal device is being disconnected, the script automatically shuts down the port.

## Steps in order to implement this feature

1. Enable iox service - link: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/guest_shell.html
   <img width="819" alt="image" src="https://github.com/CozmaSerban/iosxe-secured-port/assets/10424327/d5d6179a-6db1-4c26-84d5-36641f2fd119">
3. Enable guestshell container - link: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/guest_shell.html
   <img width="1110" alt="image" src="https://github.com/CozmaSerban/iosxe-secured-port/assets/10424327/ade71cdc-e1bf-4fc1-9fbc-ac55a777712f">
5. Copy the Python script *script.py* to the containter.
6. Create the following EEM Applet

```cli
event manager applet IF_DOWN
  event syslog pattern " %LINEPROTO-5-UPDOWN: Line protocol on Interface Gig.*down"
  action 0.0 regexp "Interface ([^,]+)" "$_syslog_msg" match intf
  action 1.0 cli command "enable"
  action 2.0 cli command "guestshell run python3 app.py $intf"
  action 3.0 cli command "end"
```

## Useful commands

Trigger the script manually to enable an interface
```cli
guestshell run python3 script.py noshut GigabitEthernet 1/0/1
```

To turn off an interface, use

```cli
guestshell run python3 script.py GigabitEthernet 1/0/1
```

The Python script keeps track of the interfaces that have been shut down or enabled manually through a *interfaces.json* file:

```json
 {
  "entry": [
    {
      "admin_up": 1,
      "interface": "GigabitEthernet 1/0/1"
    }
  ]
}
```
The variable *admin_up* is a boolean value, 1 indicating that the interface is manually enabled, 0 means the interface has been disabled. 
To track the currently shut interfaces, use from the container:
```cli
cat ./interfaces.json
```

