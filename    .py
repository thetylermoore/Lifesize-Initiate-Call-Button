#!/usr/bin/python
# coding: utf-8
import pexpect
import time
child = pexpect.spawn('telnet 1.1.1.2 2001');
time.sleep(2);
child.sendline ('2!');
#time.sleep(2);
#child.expect ('Chn2');
#time.sleep(2);
#child.sendline ('2!');
print "Input 2"
#script is designed to initiate telnet session on Extron IPL 250 to IP 1.1.1.1
#on port 2001 (direct pass through to serial port 1 - Extron SW4 HDMI)
#will change input to input 2