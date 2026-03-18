
#!/usr/bin/env python
#encoding:utf8
#
# Zabbix Server checks file count on FTP server
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

ftpServer = creds.get('FTP_APWIRADIO_SERVER')
ftpUsername = creds.get('FTP_APWIRADIO_USERNAME')
ftpPassword = creds.get('FTP_APWIRADIO_PASSWORD')

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)

count = [line for line in ftp.mlsd()]

count = len(count) - 4 # subtract folders

ftp.quit()

print(count)

