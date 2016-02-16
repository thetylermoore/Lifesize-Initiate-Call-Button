#!/usr/bin/python
# coding: utf-8
import pexpect
import time
child = pexpect.spawn('ssh auto@1.1.1.1')
time.sleep(2)
child.expect('password')
time.sleep(2)
child.sendline('pa$$w0rd')
time.sleep(2)
child.sendline ('control call dial 1111')
#time.sleep(2);
#child.expect ('Chn2');
#time.sleep(2);
#child.sendline ('2!');
time.sleep(2)
print "called x1111"
