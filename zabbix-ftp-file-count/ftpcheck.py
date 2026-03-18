#!/usr/bin/env python
#encoding:utf8
#
# Zabbix agent checks file count on FTP server
# Place in /usr/lib/zabbix/externalscripts
# 

import os
import ftplib

ftpServer = os.environ.get('FTP_APWIRADIO_SERVER')
ftpUsername = os.environ.get('FTP_APWIRADIO_USERNAME')
ftpPassword = os.environ.get('FTP_APWIRADIO_PASSWORD')

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)

count = [line for line in ftp.mlsd()]

count = len(count) - 4 # subtract folders
    
ftp.quit()

print(count)