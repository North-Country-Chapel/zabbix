#!/usr/bin/env python
#encoding:utf8
#
# Zabbix Server checks file count on Salem FTP server
#

import os
import ftplib

creds = {}
with open('/usr/lib/zabbix/externalscripts/apwi_share.creds') as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            creds[key] = value

ftpServer = creds.get('FTP_SALEM_SERVER')
ftpUsername = creds.get('FTP_SALEM_USERNAME')
ftpPassword = creds.get('FTP_SALEM_PASSWORD')
ftpDirectory = creds.get('FTP_SALEM_DIRECTORY')

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)
cwd = ftp.cwd(ftpDirectory)


count =  len(ftp.nlst())

ftp.quit()

print(count)
