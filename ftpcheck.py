#!/usr/bin/env python
#encoding:utf8
#
# Zabbix Server checks file count on FTP server
#

import os
import ftplib

ftpServer = 'ftp.applywithinradio.com'
ftpUsername = 'ncc1701@applywithinradio.com'
ftpPassword = 'zcyps4KipyfFML87j'

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)

count = [line for line in ftp.mlsd()]

count = len(count) - 4 # subtract folders

ftp.quit()

print(count)

