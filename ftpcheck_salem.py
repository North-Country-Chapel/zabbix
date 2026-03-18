#!/usr/bin/env python
#encoding:utf8
#
# Zabbix Server checks file count on FTP server
#

import os
import ftplib

ftpServer = 'home147387845.1and1-data.host'
ftpUsername = 'ftp39385561-0'
ftpPassword = 'Sal3m5329'
ftpDirectory = 'KDIA/Apply Within Radio (North County Chapel)'

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)
cwd = ftp.cwd(ftpDirectory)


count =  len(ftp.nlst())

ftp.quit()

print(count)

