# Configure Devices for Network Connectivity

Objective: To configure the Raspberry Pi to be part of a network using wireless LAN.

![network](networking/images/network.png)

Raspberry Pi Imager

![imager](networking/images/imager.png)

ping

![ping](networking/images/ping.png)

ssh

![ssh](networking/images/ssh.png)


Troubleshooting issues

```shell
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256: ***
Please contact your system administrator.
Add correct host key in /Users/macbook/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /Users/macbook/.ssh/known_hosts:2
Host key for <ip-add> has changed and you have requested strict checking.
Host key verification failed.
```

```shell
ssh-keygen -R <ip-add>
```